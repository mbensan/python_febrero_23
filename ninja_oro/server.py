from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = 'Mi Clave'


@app.route('/')
def home():
    if 'counter' not in session:
        session['counter'] = 0
    session['counter'] += 1
    return render_template('contador.html', veces=session['counter'])


@app.route('/destroy')
def destroy():
    if 'counter' in session:
        session.pop('counter')
    return redirect('/')

@app.route('/add/<num>')
def add(num):
    num = int(num)
    session['counter'] += (num - 1)
    return redirect('/')


@app.route('/add', methods=['POST'])
def add_form():
    num = int(request.form['num'])
    saludo = request.form['saludo']
    print(saludo)
    session['counter'] += (num - 1)
    return redirect('/')



if __name__ == '__main__':
    app.run(debug=True)