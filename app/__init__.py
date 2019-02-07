from flask import Flask
from flask_cors import CORS
from flasgger import Swagger, swag_from
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
    app=Flask(__name__)
    app.config.from_object(app_config[config_name])
    
    db.__init__(app)
    CORS(app)
    
    from app.auth.admin_auth.views import admin_auth 
    from app.auth.user_auth.views import user_auth
    from app.orders.views import orders 
    from app.restaurants.views import restaurants
    from app.menu.views import menu

    app.register_blueprint(admin_auth)
    app.register_blueprint(user_auth)
    app.register_blueprint(orders)
    app.register_blueprint(restaurants)
    app.register_blueprint(menu)

    return app

    
