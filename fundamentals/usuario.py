from cuenta_bancaria import CuentaBancaria

class Usuario:		# esto es lo que tenemos hasta ahora
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cuenta = CuentaBancaria()
    # agregando el método de depósito
    def deposito(self, amount):	# toma un argumento que es el monto del depósito
        self.balance += amount	# la cuenta del usuario específico aumenta en la cantidad del valor recibido
        return self

    def retiro(self, monto):
        if self.balance < monto:
            print('No tiene fondos')
            return
        self.balance -= monto
        return self
    
    def mostrar_balance(self):
        print(f'{self.name} tiene ${self.balance} en su cuenta')
        return self

    def transferir(self, usuario, monto):
        if self.balance < monto:
            print(f'No tiene suficiente dinero para transferir')
            return
        # en este punto estamos seguros que SI tenemos $
        self.retiro(monto)
        usuario.deposito(monto)
        return self

mati = Usuario('Matias', 'mbensan@codingdojo.cl')
juan = Usuario('Juan Felipe', 'jfelip@gmail.com')

mati.deposito(100).retiro(50).transferir(juan, 20).deposito(200)
# mati.retiro(50)
# mati.transferir(juan, 20)
# mati.deposito(200)
mati.mostrar_balance()

import pdb; pdb.set_trace()