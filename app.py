from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expense.db'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Expense(db.Model):
    sn = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String(50), nullable = False)
    desc = db.Column(db.String(100), nullable = False)
    amount = db.Column(db.Float, nullable = False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')







if __name__ == '__main__':
    app.run(debug = True)