from flask import Flask, render_template, request, redirect
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


@app.route('/play')
@app.route('/play/<num>')
@app.route('/play/<num>/<color>')
def play(num=3, color='aqua'):
    num = int(num)
    return render_template('play.jinja2', num=num, color=color)

@app.route('/chess')
@app.route('/chess/<columnas>')
@app.route('/chess/<columnas>/<filas>')
def chess(columnas=8, filas=8):
    columnas = int(columnas)
    filas = int(filas)
    return render_template('chess.jinja2', filas=filas, columnas=columnas)

# La ruta GET /users devuelve el HTML del formulario
@app.route('/users', methods=['GET'])
def users():
    return render_template('users.html')

# La ruta POST /users recibe los datos del formulario ya enviado
@app.route('/users', methods=['POST'])
def add_users():
    nombre = request.form['nombre']
    superpoder = request.form['superpoder']
    tipo = request.form['tipo']
        
    print(request.form)
    return 'Formulario recibido'

@app.route('/transferir', methods=['GET'])
def transferir():
    return render_template('transferir.html')


@app.route('/realizar', methods=['POST'])
def realizar_transferencia():
    nombre = request.form['nombre']
    monto = request.form['monto']
        
    print(f'Se ha transferido {monto} a la cuenta de {nombre}')
    return redirect('/transferir')



# ruta por defecto
@app.errorhandler(404)
def pagina404(err):
    return render_template('404.html')



if __name__ == '__main__':
    app.run(debug=True)
