from application import db

class Store(db.Model):
    store_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    shop_name = db.Column(db.String(50))
    shop_address = db.Column(db.String(100))
    shop_postcode = db.Column(db.String(30))
    distance_to_travel = db.Column(db.Float)
    takeaway = db.Column(db.Boolean)
    reciepts = db.relationship('Receipts', backref= 'store')
    
class Receipts(db.Model):
    receipt_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    most_expensive = db.Column(db.Float)
    cost_of_alcohol = db.Column(db.Float)
    date_of_reciept = db.Column(db.DateTime)
    receipt_total = db.Column(db.Float)
    takeaway = db.Column(db.Boolean)
    delivery_fee = db.Column(db.Float)
    delivery_time_mins = db.Column(db.Integer)
    store_id = db.Column(db.Integer, db.ForeignKey('store.store_id'), nullable=False)
    

#class Shopping_stats(db.Model):
#    stat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#    total_spent = db.Column(db.Float)
#    most_exp = db.Column(db.Float)
#    store_id = db.Column(db.Integer, db.ForeignKey('receipts.store_id'), nullable=False)









 