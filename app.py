from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
# from flask_login import login_required
import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    branch = db.Column(db.String(100), nullable=False)
    course = db.Column(db.String(100), nullable=False)
    
    def __init__(self, name, email, password,branch, course):
        self.name = name
        self.email = email
        self.branch = branch
        self.course = course
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


class teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    
    def __init__(self, name, email, password, department):
        self.name = name
        self.email = email
        self.department = department
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/admission')
def admission():
    return render_template('registeration.html')

# @app.route('/add', methods=['POST'])
# @login_required
# def add():
    

# @app.route('logout')
# def logout():
#     return redirect('/')

if __name__=='__main__':
    app.run(debug=True)