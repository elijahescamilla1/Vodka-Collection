from flask import Flask, jsonify
from config import Config
from models import db
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Vodka Collection API"})

@app.route('/vodkas', methods=['GET'])
def get_vodkas():
    return jsonify([
        {"name": "Vodka A", "origin": "Russia", "alcohol_content": 40},
        {"name": "Vodka B", "origin": "Poland", "alcohol_content": 45}
    ])

if __name__ == '__main__':
    app.run(debug=True)
