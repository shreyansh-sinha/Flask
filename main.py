'''
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/CodingThunder'
db = SQLAlchemy(app)

class Contacts(db.Model):
'''
'''
		SNo, Name, Email, Phone_Num, Message, Date
'''
'''
	SNo = db.Column(db.Integer, primary_key=True)
	Name = db.Column(db.String(80), nullable=False)
	Email = db.Column(db.String(20), nullable=False)
	Phone_Num = db.Column(db.String(10), nullable=False)
	Message = db.Column(db.String(120), nullable=False)
	Date = db.Column(db.String(12), nullable=True)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
	if(request.method == "POST"):
		name = request.form.get('name')
		email = request.form.get('email')
		phno = request.form.get('phno')
		message = request.form.get('msg')
		
		entry = Contacts(Name=name, Email=email, Phone_Num=phno, Message=message, Date=datetime.now())
		db.session.add(entry)
		db.session.commit()
		
	return render_template('contact.html')

@app.route('/post')
def services():
	return render_template('post.html')

app.run(debug=True)
'''

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/CodingThunder'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False;

db = SQLAlchemy(app)


class contacts(db.Model):
    '''
    sno, name phone_num, msg, date, email
    '''
    __tablename__ = 'contacts'
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(20), nullable=False)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        '''Add entry to the database'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        entry = contacts(name=name, phone_num = phone, msg = message,email = email )
        db.session.add(entry)
        db.session.commit()
    return render_template('contact.html')


app.run(debug=True)


