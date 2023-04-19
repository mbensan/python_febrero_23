from flask import session, redirect, render_template, Blueprint, request
from app.models.cities import City

cities = Blueprint('cities', __name__, template_folder='templates')


@cities.route('/new', methods=['POST'])
def new():
    # 1. Recibo los datos del formulario
    name = request.form['name']
    languages = request.form['languages']
    country_id = request.form['country_id']
    # 2. Uso el modelo country para crear un nuevo país
    City.add(name, languages, country_id)
    # 3. Redirigimos al remitente (pendiente) (propuesto) (agan)
    return redirect('/countries')