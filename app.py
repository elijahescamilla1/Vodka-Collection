from flask import Flask
from models import db
from flask_migrate import Migrate
from routes.auth import bp as auth_bp
from routes.vodka import bp as vodka_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(auth_bp)
app.register_blueprint(vodka_bp)

@app.before_first_request
def create_tables():
    db.create_all()

# Expose the app for Vercel
if __name__ == '__main__':
    app.run(debug=True)
else:
    # Vercel requires the app to be callable
    app = app
