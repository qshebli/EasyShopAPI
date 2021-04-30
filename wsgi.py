from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS, cross_origin

db = SQLAlchemy()
cors = CORS()

def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    db.init_app(app)
    cors.init_app(app, resources={r"*": {"origins": "*"}})
    with app.app_context():
        import Controllers  # Import routes
        db.create_all()  # Create database tables for our data models
        JWTManager(app) # connect app to JWT

        return app

app = create_app()

if __name__ == "__main__":
    app.run(port=5000)