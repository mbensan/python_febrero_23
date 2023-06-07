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
    
    def buscar(self, llave):
        if self.llave == llave:
            return self.valor
        
        elif llave < self.llave:
            if self.izq is None:
                return None
            return self.izq.buscar(llave)
        
        else: # llave > self.llave
            if self.der is None:
                return None
            return self.der.buscar(llave)
        
    def largo(self):
        if self.izq is None and self.der is None:
            return 1
        
        elif self.izq is None:
            return 1 + self.der.largo()

        elif self.der is None:
            return 1 + self.izq.largo()

        else:
            return 1 + self.izq.largo() + self.der.largo()
    
    def altura(self):
        if self.izq is None and self.der is None:
            return 1
        
        elif self.izq is None:
            return 1 + self.der.altura()

        elif self.der is None:
            return 1 + self.izq.altura()

        else:
            return 1 + max(self.izq.altura(), self.der.altura()) 


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
        if self.raiz is None:
            return None
        return self.raiz.buscar(llave)
    
    def largo(self):
        if self.raiz is None:
            return 0
        return self.raiz.largo()
    
    def altura(self):
        if self.raiz is None:
            return 0
        return self.raiz.altura()

    def min(self):
        pass


nombres = Abb()
nombres.add('Maca', 'info de Maca')
nombres.add('Kari', 'info de Kari')
nombres.add('Ricardo', 'info de Ricardo')
nombres.add('Pablo', 'info de Pablo')
nombres.add('Osvaldo', 'info de Osvaldo')
nombres.add('Rafa', 'info de Rafa')
nombres.add('Flavio', 'info de Flavio')
nombres.add('Matias', 'info de Matias')
nombres.add('Arturo', 'info de Arturo')

print(nombres.buscar('Osvaldo'))
print('número de elementos', nombres.largo())
print('altura del árbol', nombres.altura())
#import pdb; pdb.set_trace()