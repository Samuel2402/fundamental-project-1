from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

################################# Home ############################################

#@app.route('/home')
#def home():
#    return render_template('home.html')

################################## end ##############################################

if __name__ == "__main__":
    app.run(debug=True, port=5000)