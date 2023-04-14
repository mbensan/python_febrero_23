from flask import session, redirect, render_template, Blueprint, request
from models.country import Country

countries = Blueprint('countries', __name__)

@countries.route('/')
def home():
    countries_dicts = Country.get_all()
    return render_template('countries.html', countries=countries_dicts)


@countries.route('/new', methods=['POST'])
def new():
    # 1. Recibo los datos del formulario
    name = request.form['name']
    gdp = request.form['gdp']
    population = request.form['population']
    # 2. Uso el modelo country para crear un nuevo país
    Country.add(name, gdp, population)
    # 3. Redirigimos al "home" de este controlador
    return redirect('/countries')


