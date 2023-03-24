import time

class Producto:

    def __init__(self, nombre, precio, cat):
        self.id = time.time()
        self.nombre = nombre
        self.precio = precio
        self.cat = cat
    
    def update_precios(self, porcentaje, aumento=True):
        if aumento:
            self.precio *= (1 + porcentaje)
        else:
            self.precio *= (1 - porcentaje)
        return self
    
    def info(self):
        print(f'El producto {self.nombre} ({self.cat}) vale ${self.precio, 2}')


class Lista:

    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
    
    def agregar(self, prod):
        self.productos.append(prod)
        return self
    
    def eliminar(self, posicion):
        try:
            del self.productos[posicion]
        except IndexError(e):
            print('No es posible eliminar')
        return self
    
    def inflacion(self, porcentaje):
        for producto in self.productos:
            producto.update_precios(porcentaje)
        return self
    
    def liquidacion(self, categoria, porcentaje):
        for producto in self.productos:
            if producto.cat == categoria:
                producto.update_precios(porcentaje, False)
        return self


p1 = Producto('Café', 10, 'Abarrote')
p1.update_precios(0.1, False).update_precios(0.1)
p1.info()

def saludar (nombre1, nombre2, *nombres): 
    print(f'hola {nombre1}')
    print(f'hola {nombre2}')
    for nombre in nombres:
        print(f'buenos dias {nombre}')


class Mazo:

    def __init__(self, jockers=False):
        pass

    def getMano(self, num=5):
        pass

    @staticmethod
    def evaluarMano(mano):
        pass
        ## nada ->10, 1par -> 20, 2pares -> 30, tercia->40




