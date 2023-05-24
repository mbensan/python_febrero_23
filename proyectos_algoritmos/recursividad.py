'''
5! = 5*4*3*2*1 = 120
12! = 12*11*10*...*3*2*1
Formula General:
n! = n * (n - 1)!
1! = 1
'''
def factorial(num):
    # caso base
    if num == 1:
        return 1
    # llamada recursiva
    return num * factorial(num - 1)

#print(1 / (factorial(6)/(factorial(40)*factorial(34))))

def hanoi(num_discos, inicio='A', fin='C'):
    # caso base
    if num_discos == 1:
        print(f'move 1: {inicio} => {fin}')
        return
    
    palo_medio = 'ABC'.replace(inicio, '').replace(fin, '')
    # caso base 2
    if num_discos == 2:
        print(f'move 1: {inicio} => {palo_medio}')
        print(f'move 2: {inicio} => {fin}')
        print(f'move 1: {palo_medio} => {fin}')
        return
    
    hanoi(num_discos - 1, inicio, palo_medio)
    print(f'move {num_discos}: {inicio} => {fin}')
    hanoi(num_discos - 1, palo_medio, fin)


# hanoi(10)

# 1-800-TETERA => 1 800 838372
def phone_words(phone_number):
    letters = {
        '2': ['A','B','C'],
        '3': ['D','E','F'],
        '4' : ['G','H','I'],
        '5' : ['J','K', 'L'],
        '6' : ['M','N','O'],
        '7' : ['p','Q', 'R', 'S'],
        '8' : ['T','U','V'],
        '9' : ['W','X','Y', 'Z'],
        '1' : ['I'],
        '0' : ['O']
    }
    # caso base, telefono de largo 1
    if len(phone_number)  == 1:
        return letters[phone_number]
    
    # caso recursivo
    primer_digito = phone_number[0]
    otros_digitos = phone_number[1:]

    combinaciones_anteriores = phone_words(otros_digitos)
    respuesta = []

    for letter in letters[primer_digito]:
        for combinacion in combinaciones_anteriores:
            respuesta.append(letter + combinacion)

    return respuesta



print(phone_words('57'))

# num_a_romanos(57) => 'LVII'