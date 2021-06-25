from flask import Flask
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
from application import forms
################################# routes ############################################
from application import routes
############################### validators ##########################################

################################### end #############################################
