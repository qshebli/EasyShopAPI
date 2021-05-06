import json
from flask import Blueprint
from datetime import datetime as dt
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from Models.Product import Product
from wsgi import db
from werkzeug.exceptions import InternalServerError


bp = Blueprint('products', __name__)


@bp.route("/", methods=["GET"])
def get_Products():
    try:
        Products = Product.query.all()
        result = [i.serialize for i in Products]
        return jsonify(result)
    except:
        raise InternalServerError()

@bp.route("/<id>", methods=["GET"])
def get_Product(id):
    try:
        product = Product.query.filter_by(id=id).first().serialize
        return jsonify(product)
    except:
        raise InternalServerError()

@bp.route("/create", methods=["POST"])
def create():
    try:
        request_body = request.json
        
        new_product = Product(
            name= request_body["name"],
            price= request_body["price"],
            quantity= request_body["quantity"],
            status= 0,
            description= request_body["description"]
        )
        db.session.add(new_product)
        db.session.commit()

        return jsonify("created successfuly")
    except:
        raise InternalServerError()

@bp.route("/edit", methods=["POST"])
def edit():
    try:
        request_body = request.json
        product = Product.query.filter_by(id=request_body["id"]).first()

        product.name= request_body["name"]
        product.price= request_body["price"]
        product.quantity= request_body["quantity"]
        product.description= request_body["description"]

        db.session.commit()
        return jsonify("edited successfuly")
    except:
        raise InternalServerError()

@bp.route("/update_status", methods=["POST"])
def update_status():
    try:
        request_body = request.json
        product = Product.query.filter_by(id=request_body["id"]).first()
        product.status = request_body["status"]
        db.session.commit()

        return jsonify("status updated successfuly")
    except:
        raise InternalServerError()     