class Vehiculo:
    # constructor
    def __init__(self, marca, modelo, rendimiento):
        # atributos
        self.marca = marca
        self.modelo = modelo
        self.rendimiento = rendimiento
    
    # métodos
    def gasto(self, kms):
        return kms / self.rendimiento

