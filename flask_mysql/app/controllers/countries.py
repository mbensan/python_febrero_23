from flask import session, redirect, render_template, Blueprint, request
from app.models.country import Country

countries = Blueprint('countries', __name__, template_folder='templates')

@countries.route('/')
def home():
    countries_dicts = Country.get_all()
    return render_template('countries.html', countries=countries_dicts)


@countries.route('/edit/<id>')
def edit_form(id):
    country = Country.get_one(id)
    return render_template('edit_form.html', country=country)


@countries.route('/detail/<id>')
def detail_view(id):
    country = Country.get_with_cities(id)
    return render_template('detail.html', country=country)


@countries.route('/edit/<id>', methods=['POST'])
def edit(id):
    # 1. Recibo los datos del formulario
    name = request.form['name']
    gdp = request.form['gdp']
    population = request.form['population']
    # 2. Uso el modelo country para crear un nuevo país
    Country.edit(id, name, gdp, population)
    # 3. Redirigimos al "home" de este controlador
    return redirect('/countries')


@countries.route('/delete/<id>')
def delete(id):
    Country.delete(id)
    return redirect('/countries')


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


