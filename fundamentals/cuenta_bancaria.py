class CuentaBancaria:
    nombre = 'BankBoston'
    todas_las_cuentas = []

    def __init__(self, tasa=0.01, balance=0):
        self.tasa = tasa
        self.balance = balance
        CuentaBancaria.todas_las_cuentas.append(self)
    
    def deposito(self, monto):
        self.balance += monto
        return self
    
    def retiro(self, monto):
        if self.balance < monto:
            print('Fondos Insuficientes')
        else:
            self.balance -= monto
        return self
    
    def info(self):
        print(f'Balance: ${self.balance}')
        return self
    
    def interes(self):
        self.balance *= (1 + self.tasa)
        return self
    
    @classmethod
    def cambiar_nombre(cls, nuevo_nombre):
        cls.nombre = nuevo_nombre
    
    @staticmethod
    def describir(cuenta):
        cuenta.mostrar_balance()
    
    @classmethod
    def info_todas(cls):
        print('Imprimiendo INFO de TODAS las cuentas')
        for cuenta in cls.todas_las_cuentas:
            cuenta.info()

cuenta1 = CuentaBancaria(.09, 200)
cuenta1.deposito(100).deposito(200).deposito(120).retiro(50).interes().info()

cuenta2 = CuentaBancaria(.03, 500)
# 100->110->121->133.1

CuentaBancaria.info_todas()