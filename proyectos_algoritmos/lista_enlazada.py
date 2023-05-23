
# ADT: Lista
'''
- conocer el largo de la lista
- mostrar la lista
- agregarle cosas a mi lista (al principio,al final)
- sacar el primer elemento de la lista
- sacar el ultimo elemento de la lista
- eliminar cosas de la lista
- ordenar la lista
'''

# Estructura de Datos
class Node:

    def __init__(self, info):
        self.info = info
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.first = None
    
    def prepend(self, info):
        new_node = Node(info)
        new_node.next = self.first
        self.first = new_node

    def append(self, info):
        # 1. Si la lista está vacía
        if self.first is None:
            self.first = Node(info)
            return
        
        # 2. En caso que la lista NO esté vacía, avanzo hasta el último nodo
        last = self.first
        while last.next is not None:
            last = last.next
        # y agrego un nuevo nodo después del último
        last.next = Node(info)
    
    def length(self):
        raise Exception('No implementada')
    
    def print(self):
        if self.first is None:
            return 0
        
        # 2. En caso que la lista NO esté vacía, avanzo hasta el último nodo
        last = self.first
        while True:
            print(last.info)
            last = last.next
            if last is None:
                break
    
    def pop(self): # elimina y retorna el último elemento de la lista
        # 1. Si la lista está vacía
        if self.first is None:
            return None
        
        # 2. Si la lista tiene UN sólo elemento
        elif self.first.next is None:
            value = self.first.info
            self.first = None
            return value
        
        # 3. Ahora, vamos a avanzar mientras tengamos al menos 2 nodos adelante
        penultimo = self.first
        while penultimo.next.next is not None:
            penultimo = penultimo.next

        value = penultimo.next.info
        penultimo.next = None
        return value

    def dehead(self): # elimina y retorna el último elemento de la lista
        raise Exception('No implementada')



lista_super = LinkedList()
lista_super.append('Lechuga')
lista_super.append('Malaya de cerdo')
lista_super.append('Carbón')
lista_super.append('6 pack de agua mineral (red ale)')

print(f'Si sacamos el último elemento, debería ser: {lista_super.pop()}')
print(f'El resto de la lista es: ')
lista_super.print()

