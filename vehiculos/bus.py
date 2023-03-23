from vehiculo import Vehiculo

class Bus(Vehiculo):

    def __init__(self, marca, modelo, rendimiento, num_asientos, clases=['Tradicional']):
        # llamr al constructor de la clase Madre
        super().__init__(marca, modelo, rendimiento)
        self.num_asientos = num_asientos
        self.clases = clases
        self.pasajeros = 0
    
    def subir(self, nuevos_pasajeros):
        if self.num_asientos < self.pasajeros + nuevos_pasajeros:
            print(f'No es posible subir {nuevos_pasajeros} pasajeros al bus')
        else:
            self.pasajeros += nuevos_pasajeros
    
    def gasto(self, kms):
        gasto_original = super().gasto(kms)
        return gasto_original * 1.1

# Sólo se ejecuta si llamo directamente al Archivo
if __name__ == '__main__':
    bus1 = Bus('Volvo', 'B150', 2, 40, ['SemiCama', 'Cama'])
    import pdb; pdb.set_trace()
