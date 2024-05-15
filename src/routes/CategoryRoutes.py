from flask import Blueprint, render_template, current_app, abort

from src.controllers.GeneroController import GeneroController
from src.controllers.PeliculaController import PeliculaController

main = Blueprint('category_blueprint', __name__)


@main.route('/<title>/')
def home(title):
    db = current_app.config['db_connection']
    try:
        elementoGenero = GeneroController.find_by_name(db, title)
        listaPeliculas = PeliculaController.find_by_genre(db, title)
    except Exception as e:
        abort(404)
    return render_template('category.html', title= title, elementoGenero=elementoGenero, listaPelicula = listaPeliculas)
