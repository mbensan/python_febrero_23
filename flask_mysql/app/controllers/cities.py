from flask import session, redirect, render_template, Blueprint, request, flash
from app.models.cities import City

cities = Blueprint('cities', __name__, template_folder='templates')


@cities.route('/new', methods=['POST'])
def new():
    # 1. Recibo los datos del formulario
    name = request.form['name']
    languages = request.form['languages']
    country_id = request.form['country_id']
    # 2. Uso el modelo country para crear un nueva ciudad
    City.add(name, languages, country_id)
    # 3. Mandamos un mensaje "flash" indicando que la nueva ciudad ha sido agregada
    flash(f'La ciudad {name} ha sido agregada')
    # 4. Redirigimos al remitente (pendiente) (propuesto) (again)
    return redirect('/countries')
