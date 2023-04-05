from flask import Flask, render_template
from random import randint

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hola Curso!'

@app.route('/dojo')
def dos():
    return '<h3>Esta es la ruta <a href="#">Dojo</a></h3>'


@app.route('/saludo/<nombre>')
def saludar(nombre):
    return f'<h4>Hola {nombre} </h4>'

'''
@app.route('/repeat/<veces>/<palabra>')
@app.route('/repeat/<veces>/<palabra>/<nombre>')
def repeat(veces, palabra, nombre='Anónimo'):
    respuesta = f'<h3>Buenos días {nombre}</h3>'
    respuesta += '<ul>'
    for i in range(int(veces)):

        red = str(randint(0, 255))
        green = str(randint(0, 255))
        blue = str(randint(0, 255))

        color = f'rgb({red}, {green}, {blue})'

        respuesta += f'<li style="color: {color}">{palabra}</li>'
    respuesta += '</ul>'
    return respuesta
'''

@app.route('/repeat/<veces>/<palabra>')
@app.route('/repeat/<veces>/<palabra>/<nombre>')
def repeat(veces, palabra, nombre='Anónimo'):

    tonalidades = []
    
    for i in range(int(veces)):

        red = str(randint(0, 255))
        green = str(randint(0, 255))
        blue = str(randint(0, 255))

        tono = f'rgb({red}, {green}, {blue})'
        tonalidades.append(tono)

    return render_template('repeat.html', nombre=nombre, palabra=palabra, colores=tonalidades)

# ruta por defecto
@app.errorhandler(404)
def pagina404(err):
    return render_template('404.html')



if __name__ == '__main__':
    app.run(debug=True)
