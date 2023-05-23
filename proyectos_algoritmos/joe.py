clientes_ejemplo = [[10, 0], [-1, -10], [2, 4]]


def distancia (punto1, punto2):
    d_total = abs(punto1[0] - punto2[0]) + abs(punto1[1] - punto2[1])
    return d_total

def joe(clientes):
    # 1. Vamos a encontrar el cuadrante qie limita el espacio de mis respuestas
    min_x = clientes[0][0]
    max_x = clientes[0][0]
    
    min_y = clientes[0][1]
    max_y = clientes[0][1]

    for cliente in clientes:
        if cliente[0] < min_x:
            min_x = cliente[0]
        
        if cliente[0] > max_x:
            max_x = cliente[0]
        
        if cliente[1] < min_y:
            min_y = cliente[1]
        
        if cliente[1] > max_y:
            max_y = cliente[1]
    
    
    punto_optimo = []
    distancia_minima = 100000
    # ahora iremos visitando todos los puntos del cuadrante, hasta encontrar la mejor ubicación para Joe
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            punto = [x, y]
            distancia_total = 0
            for cliente in clientes:
                distancia_total += distancia(punto, cliente)
            
            if distancia_total < distancia_minima:
                distancia_minima = distancia_total
                punto_optimo = punto
    
    print(f'El punto optimo está en [{punto_optimo[0]}, {punto_optimo[1]}]')
    print(f'La disntacia a todos sus clientes es {distancia_total}')

joe(clientes_ejemplo)

'''
“La abeja (insecto volador [latin opiaras]) suele habitar {habitat (flores, bosques} cerca de la vegetacion” => False
“(()))” => False
“[{{(hola)}}]” => True
'''
def parentesis (palabra):
    pila = [] # LIFO
    for letra in palabra:
        if letra == '(' or letra == '[' or letra == '{':
            pila.append(letra)
        elif letra in [')', ']', '}']:
            if len(pila) == 0:
                return False
            ultimo = pila.pop()
            if ultimo == '(' and letra != ')':
                return False
            elif ultimo == '[' and letra != ']':
                return False
            elif ultimo == '{' and letra != '}':
                return False
    if len(pila) > 0:
        return False
    return True

isPalindrome = lambda palabra : palabra == palabra[::-1]
