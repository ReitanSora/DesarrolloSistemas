from flask import Blueprint, render_template, current_app

from src.controllers.PeliculaController import PeliculaController
from src.controllers.GeneroController import GeneroController

main = Blueprint('home_blueprint', __name__)


@main.route('/')
def home():
    db = current_app.config['db_connection']
    try:
        listaPelicula = PeliculaController.find_all(db)
        listaGenero = GeneroController.find_all(db)
    except Exception as e:
        print(e)
        raise Exception(e)
    return render_template('index.html', peliculas=listaPelicula, generos=listaGenero)
