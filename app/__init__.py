from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO
from app.config import Config

db = SQLAlchemy()
jwt = JWTManager()
socketio = SocketIO(cors_allowed_origins="*")

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    socketio.init_app(app)

    from app.routes.auth_routes import auth_bp
    from app.routes.task_routes import task_bp
    from app.routes.analytics_routes import analytics_bp
    from app.routes.frontend_routes import frontend_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(task_bp)
    app.register_blueprint(analytics_bp)
    app.register_blueprint(frontend_bp)

    return app