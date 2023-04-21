from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'Mi Clave'

from app.controllers.countries import countries
from app.controllers.cities import cities
from app.controllers.authors import authors
from app.controllers.books import books

app.register_blueprint(countries, url_prefix='/countries')
app.register_blueprint(cities, url_prefix='/cities')
app.register_blueprint(authors, url_prefix='/authors')
app.register_blueprint(books, url_prefix='/books')


if __name__ == '__main__':
    app.run(debug=True)