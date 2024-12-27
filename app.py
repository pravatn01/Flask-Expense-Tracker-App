from flask import Flask, request, render_template, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

app = Flask(__name__)
local_tz = pytz.timezone('Asia/Kathmandu')

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///expense.db'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Expense(db.Model):
    sn = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    desc = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.now(pytz.utc))  # Use pytz.utc

    def __init__(self, category, desc, amount):
        self.category = category
        self.desc = desc
        self.amount = float(amount)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        expense = Expense(request.form['category'], request.form['desc'], request.form['amount'])
        db.session.add(expense)
        db.session.commit()
        return redirect(url_for('index'))

    allexpense = Expense.query.all()

    for expense in allexpense:
        expense.date_added = expense.date_added.replace(tzinfo=pytz.utc).astimezone(local_tz)

    return render_template('index.html', allexpense=allexpense)

@app.route('/edit/<int:var>', methods=['GET', 'POST'])
def edit(var):
    if request.method == 'POST':
        expense = Expense.query.filter_by(sn=var).first()
        expense.category = request.form['category']
        expense.desc = request.form['desc']
        expense.amount = request.form['amount']
        expense.date_added = datetime.now(pytz.utc)

        db.session.add(expense)
        db.session.commit()
        return redirect('/')

    expense = Expense.query.filter_by(sn=var).first()
    return render_template('edit.html', expense=expense)

@app.route('/delete/<int:var>', methods=['GET', 'POST'])
def delete(var):
    expense = Expense.query.filter_by(sn=var).first()
    if expense:
        db.session.delete(expense)
        db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)