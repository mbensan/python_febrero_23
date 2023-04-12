from flask import Flask, render_template, request, redirect, session
from random import randint
app = Flask(__name__)

app.secret_key = 'Mi Clave'

from controllers.counter import counter
from controllers.gold import ninjagold

app.register_blueprint(counter)
app.register_blueprint(ninjagold, url_prefix='/gold')


if __name__ == '__main__':
    app.run(debug=True)