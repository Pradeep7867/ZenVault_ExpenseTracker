from app.models.db import get_db_connection

def insert_expense(amount, category, note):
    conn = get_db_connection()

    conn.execute(
        "INSERT INTO expenses (amount, category, note) VALUES (?, ?, ?)",
        (amount, category, note)
    )

    conn.commit()
    conn.close()

def get_all_expenses():
    conn = get_db_connection()

    expenses = conn.execute(
        "SELECT * FROM expenses ORDER BY date DESC"
    ).fetchall()

    conn.close()
    return expenses

def get_total_expense():
    conn = get_db_connection()
    result = conn.execute(
        "SELECT SUM(amount) as total FROM expenses"
    ).fetchone()

    conn.close()
    return result['total'] if result['total'] else 0

def get_category_summary():
    conn = get_db_connection()

    result = conn.execute(
        """
        SELECT category, SUM(amount) as total
        FROM expenses
        GROUP BY category
        """
    ).fetchall()

    conn.close()
    return result

def delete_expense(expense_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM expenses WHERE id = ?",(expense_id,))
    conn.commit()
    conn.close()

def get_expense_by_id(expense_id):
    conn = get_db_connection()

    expense = conn.execute(
        "SELECT * FROM expenses WHERE id = ?",
        (expense_id,)
    ).fetchone()

    conn.close()
    return expense


def update_expense(expense_id, amount, category, note):
    conn = get_db_connection()

    conn.execute(
        """
        UPDATE expenses
        SET amount = ?, category = ?, note = ?
        WHERE id = ?
        """,
        (amount, category, note, expense_id)
    )

    conn.commit()
    conn.close()

