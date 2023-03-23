from vehiculo import Vehiculo 

class Moto(Vehiculo):

    def __init__(self, marca, modelo, rendimiento, acoplado=False):
        super().__init__(marca, modelo, rendimiento)
        self.acoplado = acoplado