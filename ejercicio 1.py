"1. Escribir una función que calcule el máximo común divisor entre dos números."

def maximo_comun_divisor(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a


a = 40
b = 8
resultado = maximo_comun_divisor(a, b)
print( f"El maximo comun divisor de {a} y {b} es {resultado}.")

"2. Escribir una función que calcule el mínimo común múltiplo entre dos números"

"fomrula es MCM(a, b) = (a * b) / MCD (a, b)"

def minimo_comun_multiplo(a, b):
    return (a * b) / maximo_comun_divisor(a, b)

a = 20
b = 6
mcm= minimo_comun_multiplo(a , b)
print(f"El minimo comun multiplo de {a} y {b} es {mcm}")

"3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia)."

d1 = dict([
    ('Nombre', 'Carla'),
    ('Edad', '30'),
    ('Documento', '37456123'),
])

print(d1)
