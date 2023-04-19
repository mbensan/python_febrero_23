from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'Mi Clave'

from app.controllers.countries import countries
from app.controllers.cities import cities

app.register_blueprint(countries, url_prefix='/countries')
app.register_blueprint(cities, url_prefix='/cities')


if __name__ == '__main__':
    app.run(debug=True)