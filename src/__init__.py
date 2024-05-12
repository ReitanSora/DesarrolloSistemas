from flask import Flask, render_template
from flask_mysqldb import MySQL
from src.routes import HomeRoutes, SuggestRoutes

app = Flask(__name__)
db = MySQL(app)

def page_not_found(error):
    return render_template('404.html'), 404

def init_app(config):

    app.config.from_object(config)
    app.config['db_connection'] = db
    # Blueprints
    app.register_blueprint(HomeRoutes.main, url_prefix='/')
    app.register_blueprint(SuggestRoutes.main, url_prefix='/suggest')

    return app
