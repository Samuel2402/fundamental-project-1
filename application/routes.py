from application import db, app
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from application.models import Receipts, Store#, Shopping_stats
from application.forms import ReceiptForm, StoreForm
################################# routes #########################################

print('=============================== app_route ====================================')

################################# home ######################################

@app.route('/')
@app.route('/newhome')
def home(): 
    return render_template('newhome.html')

################################ create #####################################

@app.route('/addreceipt', methods=['GET', 'POST'])
def add_receipt():
    error = ""
    form = ReceiptForm()
    if request.method == 'POST':
        most_expensive = form.most_expensive.data
        cost_of_alcohol = form.cost_of_alcohol.data
        date_of_reciept = form.date_of_reciept.data
        receipt_total = form.receipt_total.data
        takeaway = form.takeaway.data
        delivery_fee = form.delivery_fee.data
        delivery_time_mins = form.delivery_time_mins.data
        store = form.store.data

        if len(str(most_expensive).rsplit('.')[-1]) == 1:
            error = "Please enter a valid 'most expensive' in form: 16.00"
        elif len(str(date_of_reciept)) == 0: #YY/MM/DD
            error = "Please enter a valid date in the form YY/MM/DD"
        elif len(str(receipt_total)) == 0 or receipt_total == 0:
            error = "Receipt total cannot be 0 or empty"
        elif takeaway==True and len(str(delivery_fee)) == 0:
            error = "Please enter delivery fee"
        elif takeaway==True and len(str(delivery_time_mins)) == 0:
            error = "Please enter delivery time"
        elif len(store)==0:
            error =  "please enter a valid store name"
        else:
            shop_ref = Store.query.filter_by(name=store.lower).first()
            #mystore = add_receipt.query.filter_by(name=form.store.data.lower).first()
            new = Receipts(most_expensive=most_expensive, cost_of_alcohol=cost_of_alcohol, date_of_reciept=date_of_reciept, receipt_total=receipt_total, takeaway=takeaway, delivery_fee=delivery_fee, delivery_time_mins=delivery_time_mins, store=store, shop=shop_ref)
            db.session.add(new)
            db.session.commit()
            return 'Receipt added!'
    return render_template('addreceipt.html', form=form, message=error)

@app.route('/addstore', methods=['GET', 'POST'])
def add_store():
    error = ""
    form = StoreForm()
    if request.method == 'POST':
        name = form.name.data
        shop_address = form.shop_address.data
        shop_postcode = form.shop_postcode.data
        takeaway = form.takeaway.data

        if len(name)==2:
            error = "please enter a valid store name"
        elif len(shop_address) == 0: #YY/MM/DD
            error = "Please enter a valid address"
        elif len(shop_postcode) == 0:
            error = "Please enter a valid Postcode"
        else:
            new = Store(name=name, shop_address=shop_address, shop_postcode=shop_postcode, takeaway=takeaway)
            db.session.add(new)
            db.session.commit()
            return 'Store added!'
    return render_template('addstore.html', form=form, message=error)

################################# read #####################################

@app.route('/readreceipts', methods=['GET'])
def read_receipts():
    #Receipts.query.all()
    receipts_string = ""
    all_receipts = Receipts.query.all()
    for receipts in all_receipts:
        receipts_string += "<br>" + str(receipts.most_expensive) + "    |    " + str(receipts.cost_of_alcohol) + "    |    " + str(receipts.date_of_reciept) + "    |    " + str(receipts.receipt_total) + "    |    " + str(receipts.date_of_reciept) + "    |    " + str(receipts.takeaway) + "    |    " + str(receipts.delivery_fee) + "    |    " + str(receipts.delivery_time_mins) +" min's" + "    |    " + str(receipts.store) 
    return render_template('readreceipts.html') + receipts_string


#Receipts.query.order_by(Reveipts.store).all()
#@app.route('/read-store')

############################### update #####################################

#@app.route('/update-receipt')
#def update(name):
#    first_game = Games.query.first()
#    first_game.name = name
#    db.session.commit()
#    return first_game.name

#@app.route('/update-store')

############################### delete #####################################

#@app_route(/delete-receipt)

#@app_route(/delete-store)

################################### end ###########################################

print('============================== after_routes ==================================')

from application import validators
