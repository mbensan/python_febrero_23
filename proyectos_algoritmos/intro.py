
def busquedaBinaria(buscado, lista, inicio=0, final=None):
    if final is None:
        final = len(lista) - 1
    
    pto_medio = floor((inicio + final) / 2)

    # si encontramos el elemento
    if lista[pto_medio] == buscado:
        return buscado
    
    elif pto_medio == inicio or pto_medio == final:
        return None
    
    elif buscado < lista[pto_medio]:
        return busquedaBinaria(buscado, lista, inicio, pto_medio)
    
    else:
        return busquedaBinaria(buscado, lista, pto_medio, final)
    


# 'house' (fuerza bruta: 4292 comparaciones)
# 'house' (búsqueda binaria: 10 comparaciones)


'''
fuerza bruta: N => Costo == O(N)

busqueda binaria: N => COsto == O(log_2_(N))

comparaciones: (1 - 10000), (0 - 5000), (2500 - 5000), (3750 - 5000), (3750 - 4375), (4063 - 4375), (4200 - 4375), (4287 - 4375), (4287 - 4331), (4287 - 4300)
'''


import math
def caput(latitud):
    radio = 6371000
    vel_angular = (2 * math.pi) / (24 * 60 * 60 )
    vel_tangencial = radio * vel_angular

    vel_tangencial = vel_tangencial / 3.6
    print(f'Sale despedido a {vel_tangencial} k/h')
