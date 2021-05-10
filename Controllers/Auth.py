import json
import hashlib
from flask import Blueprint, current_app as app
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token, create_refresh_token
from Models.User import User
from Utils.auth import authenticate
import base64
from datetime import timedelta

bp = Blueprint('auth', __name__)

@bp.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    decrypted_password = base64.b64decode(password).decode('latin1')
    user = User.query.filter_by(username=username).first()
    if authenticate(user, decrypted_password):
        access_token = create_access_token(identity=user.id, expires_delta=timedelta(minutes=60))
        refresh_token = create_refresh_token(identity=user.id, expires_delta=timedelta(minutes=43800))
        return jsonify(access_token=access_token, refresh_token=refresh_token)
    
    return jsonify({"msg": "Bad username or password"}), 401

@bp.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity=identity)
    refresh_token = create_refresh_token(identity=identity)
    return jsonify(access_token=access_token, refresh_token=refresh_token)