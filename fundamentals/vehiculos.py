
class Auto:
    tipo = 'vehículo de 4 ruedas'
    # constructor
    def __init__(self, marca, modelo, rendimiento, motor):
        # atributos
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.rendimiento = rendimiento
    
    # métodos
    def gasto(self, kms):
        return kms / self.rendimiento

tida = Auto('Nissan', 'Tida', 13, 1600)
subaru = Auto('Subaru', 'Forester', 11, 2000)
chevy = Auto('Chevrolet', 'Prisma', 12, 1400)

import pdb; pdb.set_trace()