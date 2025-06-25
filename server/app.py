from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from server.config import Config
from flask_jwt_extended import JWTManager

migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from server.models import db
    from server.models.user import User
    from server.models.guest import Guest
    from server.models.episode import Episode
    from server.models.appearance import Appearance
    
    from server.controllers.guest_controller import guest_bp
    from server.controllers.episode_controller import episode_bp
    from server.controllers.appearance_controller import appearance_bp  
    from server.controllers.auth_controller import auth_bp

    app.register_blueprint(guest_bp)
    app.register_blueprint(episode_bp)
    app.register_blueprint(appearance_bp)
    app.register_blueprint(auth_bp)

    
    db.init_app(app)
    migrate.init_app(app,db)
    jwt.init_app(app)

   
    return app 