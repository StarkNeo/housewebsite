from flask import Flask
from os import path



def create_app():
    app = Flask(__name__)
    app.config["TEMPLATES_AUTO_RELOAD"]=True
    from .views import home
    app.register_blueprint(home, url_prefix='/')
    return app

