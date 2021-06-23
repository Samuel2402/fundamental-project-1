from app import db

class Store(db.Model):
    store_id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(50))
    shop_address = db.Column(db.String(100))
    distance_to_travel = db.Column(db.Float)
    takeaway = db.Column(db.Boolean)
    reciepts = db.relationship('Store', backref= 'store_id')
    
class Receipts(db.Model):
    receipt_id = db.Column(db.Integer, primary_key=True)
    Most_expensive = db.Column(db.Integer)
    cost_of_alcohol = db.Column(db.Integer)
    date_of_reciept = db.Column(db.DateTime)
    reciept_total = db.Column(db.Integer)
    takeaway = db.Column(db.Boolean)
    delivery_fee = db.Column(db.Integer)
    delivery_time = db.Column(db.DateTime)
    store_id = db.Column(db.Integer, db.ForeignKey('store.store_id'), nullable=False)
    

#class Shoppin_stats(db.Model):
#    stat_id = db.Column(db.Integer, primary_key=True)
#    total_spent = 
#    most_exp =
#    store_id =





 