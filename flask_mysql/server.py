from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'Mi Clave'

from controllers.countries import countries

app.register_blueprint(countries, url_prefix='/countries')


if __name__ == '__main__':
    app.run(debug=True)