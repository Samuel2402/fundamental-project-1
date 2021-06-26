from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField, DecimalField, DateField, BooleanField, IntegerField
from application.validators import decimal_places, name_validator
from wtforms.validators import DataRequired



class ReceiptForm(FlaskForm):
    most_expensive = DecimalField('Enter most expensive item:', validators=[DataRequired()]) 
    cost_of_alcohol = DecimalField('Input price of alcohol:', validators=[decimal_places()])
    date_of_reciept = DateField('Input date (YY/MM/DD):', validators=[DataRequired()])
    receipt_total = DecimalField('Input total cost after deductions:', validators=[DataRequired(), decimal_places()])
    takeaway = BooleanField()
    delivery_fee = DecimalField('Delivery fee (leave blank if n/a)', validators=[decimal_places()])
    delivery_time_mins = IntegerField('Delivery time (min):', validators=[DataRequired()])
    store = StringField('Store name:', validators=[name_validator()])
    submit = SubmitField('Submit Receipt')

class StoreForm(FlaskForm):
    name = StringField('Enter Store Name:', validators=[DataRequired()])
    shop_address = StringField('Enter Store Address:', validators=[DataRequired()])
    shop_postcode = StringField('Enter Store Postcode:', validators=[DataRequired()])
    distance_to_travel = DecimalField('Distance to travel to store (Kilometers):', validators=[DataRequired(), decimal_places()])
    takeaway = BooleanField()
    submit = SubmitField('Submit Store information')

