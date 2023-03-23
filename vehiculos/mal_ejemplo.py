
class Auto:
    tipo = 'vehículo de 4 ruedas'
    # constructor
    def __init__(self, marca, modelo, rendimiento, motor):
        # atributos
        self.marca = marca
        self.modelo = modelo
        self.rendimiento = rendimiento
        self.motor = motor
    
    # métodos
    def gasto(self, kms):
        return kms / self.rendimiento

tida = Auto('Nissan', 'Tida', 13, 1600)
subaru = Auto('Subaru', 'Forester', 11, 2000)
chevy = Auto('Chevrolet', 'Prisma', 12, 1400)

class Moto:
    # constructor
    def __init__(self, marca, modelo, rendimiento, acoplado=False):
        # atributos
        self.marca = marca
        self.modelo = modelo
        self.rendimiento = rendimiento
        self.acoplado = acoplado
    
    # métodos
    def gasto(self, kms):
        return kms / self.rendimiento

class Bus:
    # constructor
    def __init__(self, marca, modelo, rendimiento, num_asientos, clases=['Tradicional']):
        # atributos
        self.marca = marca
        self.modelo = modelo
        self.rendimiento = rendimiento
        self.num_asientos = num_asientos
        self.clases = clases
        self.pasajeros = 0
    
    # métodos
    def gasto(self, kms):
        return kms / self.rendimiento
    
    def subir(self, nuevos_pasajeros):
        if self.num_asientos < self.pasajeros + nuevos_pasajeros:
            print(f'No es posible subir {nuevos_pasajeros} pasajeros al bus')
        else:
            self.pasajeros += nuevos_pasajeros




bus1 = Bus('Volvo', 'B150', 2, 40 ['SemiCama', 'Cama'])
tida = Auto('Nissan', 'Tida', 13, 1600)
subaru = Auto('Subaru', 'Forester', 11, 2000)
chevy = Auto('Chevrolet', 'Prisma', 12, 1400)

import pdb; pdb.set_trace()