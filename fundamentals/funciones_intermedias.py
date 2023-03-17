# PREGUNTA 1

x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
estudiantes[0]["last_name"] = 'Bryant'
directorio_deportes['fútbol'][0] = 'André' 
z[0]['y'] = 30


# PREGUNTA 4
dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon'],
   'estudiantes': ['Vicente', 'Eduardo', 'Maca', 'Nicolás','Flavio'],
   'cursos': ['Python Feb 23', 'MERN Enero 23', 'Data Science Dic 22', 'Mern Marzo 23']
}

def printInfo (obj):
    
    for key in obj.keys():
        name = key.upper()
        # el arreglo asociado a cada llave
        array = obj[key]
        largo_array = len(array)
        print(f'\n{largo_array} {name}')

        for item in array:
            print(f'- {item}')


printInfo(dojo)
# salida:
'''
7 UBICACIONES
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORES
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
'''


