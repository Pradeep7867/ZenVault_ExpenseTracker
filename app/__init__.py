from flask import Flask

def create_app():
    app = Flask(__name__)

    # Basic config
    app.config['SECRET_KEY'] = 'mysecretkey'

    # Register routes
    from app.routes.expense_routes import expense_bp
    app.register_blueprint(expense_bp)

    return app