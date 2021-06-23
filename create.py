from app import db
from application.models import Store, Receipts

db.drop_all()
db.create_all()

McDonalds = Store(shop_name='McDonalds', shop_address='63 Northbrook st', shop_postcode='RG14 1AE', takeaway=True)
receipt_1 = Receipts(most_expensive=5.09, cost_of_alcohol=0, date_of_reciept='2021/6/23', receipt_total=11.36, takeaway=True, delivery_fee=1.99, delivery_time_mins=28, store=McDonalds)

db.session.add(McDonalds)
db.session.add(receipt_1)
db.session.commit()

#first_receipt = Receipts.query.first()
#print(first_receipt)