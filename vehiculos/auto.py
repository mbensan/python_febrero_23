from vehiculo import Vehiculo

class Auto(Vehiculo):

    def __init__(self, marca, modelo, rendimiento, motor):
        super().__init__(marca, modelo, rendimiento)
        self.motor = motor