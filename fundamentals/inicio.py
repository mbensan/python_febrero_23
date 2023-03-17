import pdb

print('HOla curso!')

def elevar3(num):
    result = num ** 3
    return result

def elevarArr(arr):
    arr[1] = arr[1] ** 3
    return arr[1]

def fizzbuzz (limit):
    for i in range(limit):
        print('Analizando el numero ' + str(i))
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


def mayor_promedio(arr):
    sum = 0
    for num in array:
        sum = sum + num
    
    prom = sum / len(arr)

    mayores = []
    for num in array:
        if num > prom:
            mayores.append(num)
    return mayores

#fizzbuzz(100)


def saludar(func, nombre='Anónimo'):
    saludo = f'Hola {nombre}, mucho gusto!'
    func(saludo)

def write(text):
    arch = open('saludo.txt', 'w')
    arch.write(text)
    arch.close()


def var(arr):
    suma = 0
    for num in arr:
        suma += num
    prom =suma / len(arr)
    # colocando una pausa en el código
    pdb.set_trace()
    sigma = 0
    for num in arr:
        sigma += abs(num - prom)
    return sigma / prom

varianza = var([5,7,2,4,9,10])

