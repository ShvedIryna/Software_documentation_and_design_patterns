import os
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

from data_access.database import SessionLocal, init_db
from data_access.models import FinancialData

app = Flask(__name__)

init_db()

@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    offset = (page - 1) * per_page
    
    session = SessionLocal()
    total_count = session.query(FinancialData).count()
    
    transactions = session.query(FinancialData)\
        .order_by(FinancialData.date.desc())\
        .offset(offset)\
        .limit(per_page)\
        .all()
    
    has_next = total_count > (page * per_page)
    session.close()
    
    return render_template('index.html', 
                           transactions=transactions, 
                           page=page, 
                           has_next=has_next)

@app.route('/add', methods=['POST'])
def add():
    session = SessionLocal()
    new_data = FinancialData(
        date=datetime.strptime(request.form['date'], '%Y-%m-%d'),
        income=float(request.form['income']),
        expense=float(request.form['expense'])
    )
    session.add(new_data)
    session.commit()
    session.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    session = SessionLocal()
    item = session.query(FinancialData).get(id)
    if item:
        item.date = datetime.strptime(request.form['date'], '%Y-%m-%d')
        item.income = float(request.form['income'])
        item.expense = float(request.form['expense'])
        session.commit()
    session.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    session = SessionLocal()
    item = session.query(FinancialData).get(id)
    if item:
        session.delete(item)
        session.commit()
    session.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)