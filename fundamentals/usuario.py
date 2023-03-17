class Usuario:		# esto es lo que tenemos hasta ahora
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance = 0
    # agregando el método de depósito
    def deposito(self, amount):	# toma un argumento que es el monto del depósito
        self.balance += amount	# la cuenta del usuario específico aumenta en la cantidad del valor recibido

    def retiro(self, monto):
        if self.balance < monto:
            print('No tiene fondos')
            return
        self.balance -= monto
    
    def mostrar_balance(self):
        print(f'{self.name} tiene ${self.balance} en su cuenta')

    def transferir(self, usuario, monto):
        if self.balance < monto:
            print(f'No tiene suficiente dinero para transferir')
            return
        # en este punto estamos seguros que SI tenemos $
        self.retiro(monto)
        usuario.deposito(10)

mati = Usuario('Matias', 'mbensan@codingdojo.cl')
mati.deposito(200)
mati.retiro(300)
mati.mostrar_balance()