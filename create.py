from app import db
from application.models import Store, Receipts

db.drop_all()
db.create_all()



