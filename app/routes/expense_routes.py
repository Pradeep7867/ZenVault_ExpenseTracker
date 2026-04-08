import flask
from flask import Blueprint, render_template,request,redirect,url_for
from app.services.expense_service import create_expense,fetch_all_expenses,fetch_dashboard_data,remove_expense,fetch_expense,edit_expense
from app.models.db import get_db_connection

expense_bp = Blueprint('expense', __name__)

@expense_bp.route('/')
def home():
    expenses = fetch_all_expenses()
    dashboard = fetch_dashboard_data()
    return render_template(
        'index.html',
        expenses=expenses,
        total=dashboard["total"],
        category_data=dashboard["category_data"]
    )

@expense_bp.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        amount = request.form.get('amount')
        category = request.form.get('category')
        note = request.form.get('note')

        # Temporary print (next step: service call)
        create_expense(amount, category, note)

        return redirect(url_for('expense.home'))

    return render_template('add_expense.html')

@expense_bp.route('/delete/<int:id>')
def delete_expense(id):
    remove_expense(id)
    return redirect(url_for('expense.home'))

@expense_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        amount = request.form.get('amount')
        category = request.form.get('category')
        note = request.form.get('note')

        edit_expense(id, amount, category, note)
        return  redirect(url_for('expense.home'))

    expense = fetch_expense(id)
    return render_template('edit_expense.html', expense=expense)



@expense_bp.route('/init-db')
def init_db():
    conn = get_db_connection()

    conn.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL,
            category TEXT,
            note TEXT,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()

    return "DB Initialized"