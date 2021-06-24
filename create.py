from app import db
from application.models import Store, Receipts

db.drop_all()
db.create_all()

#adding store to db
mcdonalds_newbury = Store(shop_name='McDonalds', shop_address='63 Northbrook st', shop_postcode='RG14 1AE', takeaway=True)
tesco_newbury_superstore1 = Store(shop_name='Tesco', shop_address='London rd, Newbury', shop_postcode='RG14 2BP', takeaway=False)

#adding receipts to db
receipt1 = Receipts(most_expensive=5.09, cost_of_alcohol=0, date_of_reciept='2021/6/23', receipt_total=11.36, takeaway=True, delivery_fee=1.99, delivery_time_mins=28, store=mcdonalds_newbury)

#stores
db.session.add(mcdonalds_newbury)
db.session.add(tesco_newbury_superstore1)
#receipts
db.session.add(receipt1)

#db.session.add_all(McDonalds,receipt1)
db.session.commit()

#first_receipt = Receipts.query.first()
#print(first_receipt)