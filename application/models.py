from app import db

class Store(db.Model):
    store_id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(50))
    shop_address = db.Column(db.String(100))
    shop_postcode = db.Column(db.String(30))
    distance_to_travel = db.Column(db.Float)
    takeaway = db.Column(db.Boolean)
    reciepts = db.relationship('Receipts', backref= 'store')
    
class Receipts(db.Model):
    receipt_id = db.Column(db.Integer, primary_key=True)
    most_expensive = db.Column(db.Float)
    cost_of_alcohol = db.Column(db.Float)
    date_of_reciept = db.Column(db.DateTime)
    receipt_total = db.Column(db.Float)
    takeaway = db.Column(db.Boolean)
    delivery_fee = db.Column(db.Float)
    delivery_time_mins = db.Column(db.Integer)
    store_id = db.Column(db.Integer, db.ForeignKey('store.store_id'), nullable=False)
    

#class Shoppin_stats(db.Model):
#    stat_id = db.Column(db.Integer, primary_key=True)
#    total_spent = 
#    most_exp =
#    store_id =





 