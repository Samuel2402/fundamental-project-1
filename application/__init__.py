from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField, DateField, BooleanField, IntegerField
from flask_sqlalchemy import SQLAlchemy
import os
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#app.config['SECRET_KEY'] = getenv('SKEY')

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)

################################# Forms #############################################

class ReceiptForm(FlaskForm):
    most_expensive = DecimalField('Enter most expensive item:')
    cost_of_alcohol = DecimalField('Input price of alcohol:')
    date_of_reciept = DateField('Input Date:')
    receipt_total = DecimalField('Input total cost after deductions:')
    takeaway = BooleanField()
    delivery_fee = DecimalField('Delivery fee (leave blank if n/a)')
    delivery_time_mins = IntegerField('Delivery time (min):')
    submit = SubmitField('Submit Receipt')

class StoreForm(FlaskForm):
    shop_name = StringField('Enter Store Name:', maxlength=30)
    shop_address = StringField('Enter Store Address:', maxlength=50)
    shop_postcode = StringField('Enter Store Postcode:', maxlength=10)
    distance_to_travel = DecimalField('Distance to travel to store (Kilometers):')
    takeaway = BooleanField('Takeaway (True/False):')
    submit = SubmitField('Submit Store information')

print('================================app.py======================================')

################################# routes ############################################
from application import routes
################################## end ##############################################
