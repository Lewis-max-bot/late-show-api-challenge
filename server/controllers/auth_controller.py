from flask import Blueprint, request, jsonify
from server.models import db
from server.models.user import User
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint('auth_bp', __name__, url_prefix="/auth")

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({ "error": "Username and password required" }), 400

    if User.query.filter_by(username=username).first():
        return jsonify({ "error": "Username already exists" }), 409

    hashed_password = generate_password_hash(password)
    user = User(username=username, password_hash=hashed_password)
    db.session.add(user)
    db.session.commit()

    return jsonify({ "message": "User created successfully" }), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({ "error": "Invalid credentials" }), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({ "access_token": access_token }), 200
