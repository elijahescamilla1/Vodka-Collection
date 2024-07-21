from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from models import db, User, Vodka
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by(username=data['username']).first():
        return jsonify({"msg": "User already exists"}), 400
    new_user = User(username=data['username'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "User created successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Bad username or password"}), 401

@app.route('/vodkas', methods=['GET'])
@jwt_required()
def get_vodkas():
    vodkas = Vodka.query.all()
    return jsonify([vodka.to_dict() for vodka in vodkas]), 200

@app.route('/vodkas', methods=['POST'])
@jwt_required()
def add_vodka():
    data = request.get_json()
    new_vodka = Vodka(name=data['name'], brand=data['brand'], country=data['country'], price=data['price'])
    db.session.add(new_vodka)
    db.session.commit()
    return jsonify(new_vodka.to_dict()), 201

@app.route('/vodkas/<int:id>', methods=['PUT'])
@jwt_required()
def update_vodka(id):
    data = request.get_json()
    vodka = Vodka.query.get_or_404(id)
    vodka.name = data['name']
    vodka.brand = data['brand']
    vodka.country = data['country']
    vodka.price = data['price']
    db.session.commit()
    return jsonify(vodka.to_dict()), 200

@app.route('/vodkas/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_vodka(id):
    vodka = Vodka.query.get_or_404(id)
    db.session.delete(vodka)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
