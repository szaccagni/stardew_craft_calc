from flask import Flask
from flask.cli import with_appcontext

from config import Config
from app.extensions import db

from db_utils import add_ingredients, add_recipe_ingredients

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)

    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.recipes import bp as recipes_bp
    app.register_blueprint(recipes_bp, url_prefix='/recipes')

    @app.cli.command("init-db")
    def update_db_cmd():    
        db.drop_all()
        db.create_all()
        add_ingredients()
        add_recipe_ingredients()

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app