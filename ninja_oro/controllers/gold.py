from flask import session, redirect, render_template, Blueprint, request

ninjagold = Blueprint('ninjagold', __name__)


@ninjagold.route('/')
def gold():
    if 'gold' not in session:
        session['gold'] = 0
    if 'messages' not in session:
        session['messages'] = []

    return render_template('gold.html', gold=session['gold'], messages=session['messages'])


@ninjagold.route('/process_money', methods=['POST'])
def process_money():
    # 1. Recibo los datos del formulario
    mingold = request.form['mingold']
    maxgold = request.form['maxgold']
    lugar = request.form['lugar']

    # 2. Los transformo a entero
    mingold = int(mingold)
    maxgold = int(maxgold)

    # 3. Genero el numero de oros al axar que ganó el usuario
    ganancia = randint(mingold, maxgold)

    # 4. Le sumo la ganancia al total de oros del usuario
    session['gold'] += ganancia

    # 5. Agrego el mensaje correspondiente
    if ganancia > 0:
        session['messages'].append(f'Ganaste {str(ganancia)} en {lugar}')
    else:
        session['messages'].append(f'Perdiste {str(-ganancia)} en {lugar}')

    print(f'El minimo es {mingold} y el maximo es {maxgold}')
    return redirect('/gold')