from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    jwt.init_app(app)

    from .routes import mood, recipes, auth, user, analytics, social, ai_recipe, grocery
    app.register_blueprint(mood.bp, url_prefix='/api/mood')
    app.register_blueprint(recipes.bp, url_prefix='/api/recipes')
    app.register_blueprint(auth.bp, url_prefix='/api/auth')
    app.register_blueprint(user.bp, url_prefix='/api/users')
    app.register_blueprint(analytics.bp, url_prefix='/api/analytics')
    app.register_blueprint(social.bp, url_prefix='/api/social')
    app.register_blueprint(ai_recipe.bp, url_prefix='/api/recipes/generate')
    app.register_blueprint(grocery.bp, url_prefix='/api/grocery')

    return app
