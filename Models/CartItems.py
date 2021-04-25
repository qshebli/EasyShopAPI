"""Data models."""
from wsgi import db
from Utils.date import dump_datetime

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
        return {
            'id': self.id,
            'cid': self.cid,
            'pid': self.pid,
            'quantity': self.quantity,
            'status': self.status
        }

    def __repr__(self):
        return "<CartItems {}>".format(self.id)
  
