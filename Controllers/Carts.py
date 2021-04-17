import json
import hashlib
from flask import Blueprint
from datetime import datetime as dt
from flask import jsonify, request
from flask_jwt_extended  import jwt_required, get_jwt_identity
from wsgi import db
from Models.Carts import Cart
from Models.CartItems import CartItems
from Models.User import User
from werkzeug.exceptions import InternalServerError

bp = Blueprint('carts', __name__)

@bp.route("/", methods=["GET"])
def get_Carts():
    try:
        Carts = Cart.query.all()
        result = [i.serialize for i in Carts]
        return jsonify(result)
    except:
        raise InternalServerError()

@bp.route("/add_to_cart", methods=["POST"])
@jwt_required()
def add_to_cart():
    request_body = request.json
    user_id = get_jwt_identity()
    user_cart = Cart.query.filter_by(uid=user_id, status=0).first()
    
    if user_cart is None:
        user_cart = create_cart(user_id)
    
    new_cart_item = CartItems(
        cid= user_cart.id,
        pid= request_body["pid"],
        quantity= request_body["quantity"],
        status= 0
    )

    db.session.add(new_cart_item)
    db.session.commit()

    return jsonify("item added successfuly")

@bp.route("/remove_from_cart", methods=["post"])
def remove_from_cart():
    request_body = request.json
    item_id = int(request_body["id"])
    item_to_remove = CartItems.query.filter_by(id=item_id).first()


    db.session.delete(item_to_remove)
    db.session.commit()

    return jsonify("item removed successfuly")

def create_cart(user_id):
    new_cart = Cart(
        uid = user_id,
        timestamp = dt.now(),
        status = 0
    )
    db.session.add(new_cart)
    db.session.commit()
    new_cart = Cart.query.filter_by(uid=user_id, status=0).first()
    return new_cart