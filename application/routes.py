from application import db, app
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from application.models import Receipts, Store#, Shopping_stats
from application import ReceiptForm
################################# routes #########################################

print('===============================app_route====================================')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home/add-receipt', methods=['GET', 'POST'])
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

        if len(most_expensive) == 0 or most_expensive == 0:
            error = "please enter a valid Decimal price"
        elif len(date_of_reciept) <= 7:
            error = "Please enter a valid date in the form YY/MM/DD"
        elif len(receipt_total) == 0 or receipt_total == 0:
            error = "Receipt total cannot be 0 or empty"
        elif takeaway==True and len(takeaway) == 0:
            error = "Please enter delivery fee"
        else:
            return 'thank_you'

    return render_template('add-receipt.html', form=form, message=error)

print('==============================after_route===================================')

################################### end ###########################################

