from app.models.expensive_model import insert_expense,get_all_expenses,get_category_summary,get_total_expense,get_expense_by_id,update_expense ,delete_expense
from datetime import datetime

def create_expense(amount, category, note):
    insert_expense(amount, category, note)
    return True
# Date time Format
def format_date(date_value):
    dt = datetime.strptime(date_value, "%Y-%m-%d %H:%M:%S")
    return dt.strftime("%b %d, %Y")   # Oct 22, 2023

def fetch_all_expenses():
    expenses = get_all_expenses()
    formatted_expenses = []
    for e in expenses:
        e = dict(e)
        e["formatted_date"] = format_date(e["date"])
        e['txn_id'] = format_txn_id(e['id'])
        e['formatted_amount'] = format_amount(e['amount'])
        formatted_expenses.append(e)

    return formatted_expenses

def fetch_dashboard_data():
    total = get_total_expense()
    category_data = get_category_summary()

    formatted_data = []

    for c in category_data:
        c = dict(c)

        # % calculation
        percentage = (c['total'] / total) * 100 if total else 0

        c['percentage'] = round(percentage)

        # formatted amount
        c['formatted_total'] = format_amount(c['total'])

        formatted_data.append(c)

    return {
        "total": total,
        "category_data": formatted_data
    }

def remove_expense(expense_id):
    delete_expense(expense_id)

def fetch_expense(expense_id):
    return get_expense_by_id(expense_id)

def edit_expense(expense_id,amount,category,note):
    update_expense(expense_id,amount,category,note)

def format_txn_id(expense_id):
    return f"TXN-{expense_id:03d}"

def format_amount(amount):
    amount = float(amount)
    return "{:,.0f}".format(amount)