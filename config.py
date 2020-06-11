import os

class Config():
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jefferson:Jefferson_22@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
class ProdConfig(Config):

    pass
class DevConfig(Config):
       DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,    
}            