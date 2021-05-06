"""Data models."""
from wsgi import db
from Utils.date import dump_datetime

class Product(db.Model):
    """Data model for Products."""

    __tablename__ = "Product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    price = db.Column(db.Numeric(18,0), index=False, unique=False, nullable=False)
    quantity = db.Column(db.Integer, index=False, unique=False, nullable=False)
    status = db.Column(db.Integer, index=False, unique=False, nullable=False)
    description = db.Column(db.Text, index=False, unique=False, nullable=False)
    

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'name': self.name,
            'price': str(self.price),
            'quantity': self.quantity,
            'status': self.status,
            'description':self.description
        }

    def __repr__(self):
        return "<Product {}>".format(self.name)
