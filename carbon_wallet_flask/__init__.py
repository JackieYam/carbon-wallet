from flask import Flask
from config import Config
from carbon_wallet_flask.models import db

def create_app():
   app = Flask(__name__, instance_relative_config=True)
   app.config.from_object(Config)

   db.init_app(app)

   # Import and register routes
   from carbon_wallet_flask.routes.test import test
   app.register_blueprint(test)

   return app
