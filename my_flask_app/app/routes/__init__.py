from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your-secret-key'

    from app.routes import auth_bp  # Đã được export từ routes/__init__.py
    app.register_blueprint(auth_bp)

    return app
