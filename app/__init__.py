from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from config import config_options
from flask_uploads import UploadSet,configure_uploads,IMAGES


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()
photos = UploadSet('photos',IMAGES)



def create_app(config_name):
    
  app = Flask(__name__)
  
  app.config.from_object(config_options[config_name])
  
#   from .auth import auth as auth_blueprint
#   app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
#   db.init_app(app)
  bcrypt.init_app(app)
  login_manager.init_app(app)
  mail.init_app(app)


  from app.users.views import users
  from app.pitches.views import pitches
  from app.main.views import main


  app.register_blueprint(users)
  app.register_blueprint(pitches)
  app.register_blueprint(main)

  return app




