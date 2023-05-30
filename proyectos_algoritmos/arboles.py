class Nodo:

    def __init__(self, llave, valor=None):
        self.llave = llave
        self.valor = valor
        self.izq = None
        self.der = None
    
    def add(self, llave, valor):
        # si la llave es menor, se agrega a la izquierda
        if llave < self.llave:
            if self.izq is None:
                self.izq = Nodo(llave, valor)
            else:
                self.izq.add(llave, valor)
        
        elif llave > self.llave:
            if self.der is None:
                self.der = Nodo(llave, valor)
            else:
                self.der.add(llave, valor)


class Abb:

    def __init__(self):
        self.raiz = None
    
    def add(self, llave, valor=None):
        # si el árbol está vacío, creamos el primer Nodo
        if self.raiz is None:
            self.raiz = Nodo(llave, valor)
            return
        
        # caso en que ya existe una raíz
        self.raiz.add(llave, valor)
    
    def buscar(self, llave):
        pass
    
    def largo(self):
        pass
    
    def altura(self):
        pass

    def min(self):
        pass




nombres = Abb()
nombres.add('Maca')
nombres.add('Kari')
nombres.add('Ricardo')
nombres.add('Pablo')
nombres.add('Osvaldo')
nombres.add('Rafa')
nombres.add('Flavio')
import pdb; pdb.set_trace()