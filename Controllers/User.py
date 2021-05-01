import json
import hashlib
import base64
from flask import Blueprint, current_app as app
from datetime import datetime as dt
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from Models.User import User
from wsgi import db
from werkzeug.exceptions import InternalServerError
from Utils.auth import authenticate

bp = Blueprint('users', __name__)

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    decrypted_password = base64.b64decode(password).decode('latin1')
    user = User.query.filter_by(username=username).first()
    if authenticate(username, decrypted_password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)
    
    return jsonify({"msg": "Bad username or password"}), 401

@bp.route("/", methods=["GET"])
def get_users():
    try:
        users = User.query.all()
        result = [i.serialize for i in users]
        return jsonify(result)
    except:
        raise  InternalServerError()

@bp.route("/create", methods=["POST"])
@jwt_required()
def create():
    try:
        request_body = request.json
        hashed_password = hashlib.md5(request_body["password"].encode('utf-8')).hexdigest()
        new_user = User(
            username= request_body["username"],
            password= hashed_password,
            role= request_body["role"],
            isLocked = 0,
            createdBy= get_jwt_identity(),
            createdAt= dt.now()
            )
        db.session.add(new_user)
        db.session.commit()
        return jsonify("created successfuly")
    except:
        raise InternalServerError()

@bp.route("/register", methods=["POST"])
def register():
    try:
        request_body = request.json
        hashed_password = hashlib.md5(request_body["password"].encode('utf-8')).hexdigest()
        new_user = User(
            username= request_body["username"],
            password= hashed_password,
            role= '1',
            isLocked = 0,
            createdBy= '1',
            createdAt= dt.now()
            )
        db.session.add(new_user)
        db.session.commit()
        return jsonify("registerd successfuly")
    except:
        raise InternalServerError()