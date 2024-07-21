from flask import Flask
from models import db
from flask_migrate import Migrate
from routes.auth import bp as auth_bp
from routes.vodka import bp as vodka_bp
from config import Config
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(vodka_bp, url_prefix='/vodkas')

    @app.before_first_request
    def create_tables():
        db.create_all()

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
