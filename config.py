import os

class Config:


    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY='1234567890'
    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    MAIL_USE_TLS = True
        #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'pitch'
    SENDER_EMAIL = 'cheruiyotedah@gmail.com'
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    
        # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    # @staticmethod
    # def init_app(app):
    #     pass


    
class TestConfig(Config):
  # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitch_test'
  pass
  
  




class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass



class DevConfig(Config):
  
   
 
  DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig

}
