from flask import Blueprint, render_template

main = Blueprint('suggest_blueprint',__name__)

@main.route('/')
def suggest():
    return render_template('suggest.html')