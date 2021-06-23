from app import app, db
from appliation.models import 

@app.route('/home')
def home():
    return render_template('home.html')