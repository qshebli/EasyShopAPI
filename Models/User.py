"""Data models."""
from wsgi import db
from Utils import dump_datetime

class User(db.Model):
    """Data model for user accounts."""

    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), index=True, unique=True, nullable=False)
    password = db.Column(db.String(200), index=False, unique=False, nullable=False)
    role = db.Column(db.Integer, index=False, unique=False, nullable=False)
    isLocked = db.Column(db.Integer, index=False, unique=False, nullable=False)
    createdBy = db.Column(db.String(200), index=False, unique=False, nullable=False)
    createdAt = db.Column(db.DateTime, index=False, unique=False, nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        created_by = User.query.filter_by(id=int(self.createdBy)).first()
        created_by_name = ''
        if created_by:
            created_by_name = created_by.username
        return {
            'id': self.id,
            'username': self.username,
            'role': self.role,
            'createdBy': {'id': self.createdBy, 'username': created_by_name},
            'createdAt': dump_datetime(self.createdAt)
        }

    def __repr__(self):
        return "<User {}>".format(self.username)