"""Data models."""
from wsgi import db
from Utils.date import dump_datetime

class Cart(db.Model):
    """Data model for carts."""

    __tablename__ = "Cart"
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, index=True, unique=False, nullable=False)
    timestamp = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    status = db.Column(db.Integer, index=False, unique=False, nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'uid': self.uid,
            'timestamp': self.timestamp,
            'status': self.status
        }

    def __repr__(self):
        return "<Cart {}>".format(self.id)
  
