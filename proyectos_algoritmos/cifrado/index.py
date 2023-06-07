# C E N I T
# P O L A R

'''
el tesoro esta bajo la cama
on rosete
'''

from PIL import Image

def cenit_polar(palabra):
    encriptada = ''
    dd = {
        'c': 'p',
        'e': 'o',
        'n': 'l',
        'i': 'a',
        't': 'r',
        'p': 'c',
        'o': 'e',
        'l': 'n',
        'a': 'i',
        'r': 't'
    }
    for letra in palabra.lower():
        letra_encriptada = dd.get(letra, letra)
        encriptada += letra_encriptada
    
    return encriptada

#print(cenit_polar(cenit_polar('cuidado, te estan siguiendo')))

mensaje = "hola curso" # de largo 80 en binario

def text2binary(palabra):
    palabra_bin = ''
    for letra in palabra:
        letra_bin = format(ord(letra), '08b')
        palabra_bin += letra_bin
    return palabra_bin

def binary2text(palabra_bin):
    palabra = ''
    for i in range(0, len(palabra_bin), 8):
        trozo = palabra_bin[i: i+8]
        letra = chr(int(trozo, 2))
        palabra += letra

    return palabra

def cifrar (mensaje, ruta_imagen):
    # 1. Transformamos el mensjae a binario
    mensaje_bin = text2binary(mensaje + '0')

    # 2. Abrimos la imagen y su mapa de pixeles
    imagen = Image.open(ruta_imagen)
    pixel_map = imagen.load()

    # 3. Vamos letra por letra del binario, modificando 1 pixel a la vez
    coord_x = 100
    coord_y = 100

    for letra in mensaje_bin:
        # 4. Obtener los colores originales de este pixel
        red = pixel_map[coord_x, coord_y][0]
        green = pixel_map[coord_x, coord_y][1]
        blue = pixel_map[coord_x, coord_y][2]
        alpha = pixel_map[coord_x, coord_y][3]

        # 5. Modificamos el "green" dependiendo de la letra que sea
        if letra == '0':
            if green % 2 != 0:
                green -= 1
        
        else: # letra == '1'
            if green % 2 != 1:
                green += 1
        
        # 6. Modificamos el pixel complento
        pixel_map[coord_x, coord_y] = (red, green, blue, alpha)
        coord_x += 1
    
    imagen.save('mensaje.png')


def descifrar(ruta_imagen):
    finalizador = '00110000'
    intentos = 20

    # 1. Abrimos la imagen y su mapa de pixeles
    imagen = Image.open(ruta_imagen)
    pixel_map = imagen.load()

    # fijamos nuestro punto de partida
    coord_x = 100
    coord_y = 100

    mensaje_bin = ''

    while True:
        
        letra_bin = ''
        for i in range(8):
            green = pixel_map[coord_x + i, coord_y][1]
            if green % 2 == 0:
                letra_bin += '0'
            else:
                letra_bin += '1'
        
        if letra_bin == finalizador or intentos == 0:
            break

        mensaje_bin += letra_bin
        coord_x += 8
        intentos -= 1
    
    print(binary2text(mensaje_bin))


#cifrar('viva tchile', 'bosque.png')
descifrar('mensaje.png')