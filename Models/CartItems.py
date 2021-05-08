"""Data models."""
from wsgi import db
from Utils.date import dump_datetime
from .Product import Product

class CartItems(db.Model):
    """Data model for carts."""

    __tablename__ = "CartItems"
    id = db.Column(db.Integer, primary_key=True)
    cid = db.Column(db.Integer, index=True, unique=False, nullable=False)
    pid = db.Column(db.Integer, index=False, unique=False, nullable=False)
    quantity = db.Column(db.Integer, index=False, unique=False, nullable=False)
    status = db.Column(db.Integer, index=False, unique=False, nullable=False)
    
    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        product = Product.query.filter_by(id=int(self.pid)).first()
        product_name = ''
        product_price = ''
        if product:
            product_name = product.name
            product_price = product.price
        return {
            'id': self.id,
            'cid': self.cid,
            'product': {
                'id': self.pid,
                'name': product_name,
                'price': str(product_price)
            },
            'quantity': self.quantity,
            'status': self.status
        }

    def __repr__(self):
        return "<CartItems {}>".format(self.id)
  
