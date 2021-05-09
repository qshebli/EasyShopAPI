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
        status_str = ''
        if self.status == 0:
            status_str = 'in progress'
        elif self.status == 1:
            status_str = 'approved'
        elif self.status == 2 :
            status_str = 'rejected' 
        return {
            'id': self.id,
            'name': self.name,
            'price': str(self.price),
            'quantity': self.quantity,
            'status': {
                'status_code': self.status, 
                'status': status_str
            },
            'description':self.description
        }

    def __repr__(self):
        return "<Product {}>".format(self.name)
