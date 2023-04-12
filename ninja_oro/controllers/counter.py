from flask import session, redirect, render_template, Blueprint, request

counter = Blueprint('couter', __name__)

@counter.route('/')
def home():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1
    return render_template('contador.html', veces=session['counter'])


@counter.route('/destroy')
def destroy():
    if 'counter' in session:
        session.pop('counter')
    return redirect('/')

@counter.route('/add/<num>')
def add(num):
    num = int(num)
    session['counter'] += (num - 1)
    return redirect('/')


@counter.route('/add', methods=['POST'])
def add_form():
    num = int(request.form['num'])
    saludo = request.form['saludo']
    print(saludo)
    session['counter'] += (num - 1)
    return redirect('/')
