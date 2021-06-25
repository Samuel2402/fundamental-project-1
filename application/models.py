from application import db

print("============================ Before Models.py ================================")

class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    shop_address = db.Column(db.String(100))
    shop_postcode = db.Column(db.String(30))
    takeaway = db.Column(db.Boolean)
    receipt = db.relationship('Receipts', backref='shop')

class Receipts(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    most_expensive = db.Column(db.Float)
    cost_of_alcohol = db.Column(db.Float)
    date_of_reciept = db.Column(db.DateTime)
    receipt_total = db.Column(db.Float)
    takeaway = db.Column(db.Boolean)
    delivery_fee = db.Column(db.Float)
    delivery_time_mins = db.Column(db.Integer)
    store = db.Column(db.String(30), db.ForeignKey('store.name'), nullable=False)

#class Shopping_stats(db.Model):
#    stat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#    total_spent = db.Column(db.Float)
#    most_exp = db.Column(db.Float)
#    store_id = db.Column(db.Integer, db.ForeignKey('receipts.store_id'), nullable=False)


print("============================= after Models.py ================================")




 