from flask import Flask
from app.models.db import get_db_connection

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'mysecretkey'

    from app.routes.expense_routes import expense_bp
    app.register_blueprint(expense_bp)

    # AUTO CREATE TABLE
    with app.app_context():
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

    return app