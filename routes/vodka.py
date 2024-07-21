from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from models import db, Vodka

bp = Blueprint('vodka', __name__, url_prefix='/vodkas')

@bp.route('/', methods=['GET'])
@jwt_required()
def get_vodkas():
    vodkas = Vodka.query.all()
    return jsonify([vodka.to_dict() for vodka in vodkas]), 200

@bp.route('/', methods=['POST'])
@jwt_required()
def add_vodka():
    data = request.get_json()
    new_vodka = Vodka(name=data['name'], brand=data['brand'], country=data['country'], price=data['price'])
    db.session.add(new_vodka)
    db.session.commit()
    return jsonify(new_vodka.to_dict()), 201

@bp.route('/<int:id>', methods=['PUT'])
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

@bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_vodka(id):
    vodka = Vodka.query.get_or_404(id)
    db.session.delete(vodka)
    db.session.commit()
    return '', 204
