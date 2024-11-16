#int es para números enteros
#float es para números reales
#type es una función que nos devuelve el tipo de variable que tenemos (float, int, str, etc)
#La potencia es con los dos asteriscos: 3*2 = 6 y 3**2 = 9
#Cuando divides dos números enteros, te devuelve un float -> 9/3 = 3.0
#Se puede hacer conversión de tipos: int(9/3) = 3
#Si haces int de un número no entero, la función int actúa como la función suelo (lo trunca)
#4%2 es 4 (mod2), es decir, devuelve el resto de la división 
#podemos utilizar paréntesis para alterar el orden de las operaciones 
# el signo = es una asignación (nos guarda un dato en la memoria a través de variables)

#Calculamos el área de una circunferencia de radio 2
pi = 3.14159
radio = 2
area = pi * (radio ** 2)
#Debemos darles nombres descriptivos a las variables por si nos hemos equivocado y poder encontrar más fácilmente el error

#Si queremos crear distintos radios e imprimir las distintas áreas:
pi = 3.14
radio_1 = 2
radio_2 = 1
area_1 = pi * (radio_1 ** 2)
area_2 = pi * (radio_2 ** 2)
print(area_1, area_2)
#recordar que el ordenador lee las órdenes de arriba a abajo

#nombres que no pueden ser variables: no puedes usar palabras reservadas (while, print, etc., solo numeros o numeros y luego una letra (la letra tiene que ir delante de los números)) porque el intertérprete puede confundirse

# si tenemos 
pi = 3.14
radio = 2
area = pi * (radio ** 2)
area_R = area
area = area +1
print(area_R, area)
#vamos a tener que area_R y area son dos valores distintos porque python ejecuta de arriba a abajo, por tanto, area_R va a ser pi*(radio**2) y area va a ser area_R+1.

#area = area+1 también se puede escribir como area += 1. Esta notación funciona para el resto de operaciones aritméticas

a = input('Your age')
print(a)

#PyCharm user name = toritorroja23; password = 9yk4c5JK+?

#18/10/24

# la función == si que funciona con distintos tipos de objetos, sin embargo el < y el > no.

1 == "weywey" #esto da falso

not a #es True si a es False
a and b #True si ambos son True
a or b # True si a o b son True

age = int(input("Introduce tu edad:"))
if age >= 18:
    print("Ya eres mayor de edad")
else: #age < 18
    if age = 17:
        print("Estas a punto de ser mayor de edad")
    else:
        print("You are still a little baby!")
#en vez de usar el primer else podemos hacer
if age >= 18:
    print("Ya eres mayor de edad")
elif age = 17:
    print("Estas a punto de ser mayor de edad")
else:
    print("You are still a little baby!")
#si tienes varios elif's seguidos y uno cubre a otro, se ejecuta el primero
#si escribes varios if's en vez de elif's, el else se corresponde con el último if

#21/10/24

# vamos a ver como importar librerias

import math #esto importa la libreria math
print(math.sqrt(16))

#si quieres importar funciones especificas y no toda la libreria:
from math import exp, sqrt
print(exp(1))
print(sqrt(4))
#no hace falta poner math.exp ni math.sqrt

#también puedes hacer
from math import exp as my_exp #le cambias el nombre a la función

#definir funciones
def ejemplo():
    #codigo del ejemplo
ejemplo() #así se ejecuta el ejemplo

def hoja2_ej1_sol1():
    n1 = int(input("Introduce un numero"))
    n2 = int(input("Introduce un numero"))
    n3 = int(input("Introduce un numero"))

    if n1 <= n2 <= n3:
        minimo, medio, maximo = n1, n2, n3
    elif n1 <= n2 <= n3:
        # ...
    #hacemos todos los casos posibles
    print(minmo, ",", medio, ",", maximo)

def hoja2_ej1_sol2():
    n1 = int(input("Introduce un numero"))
    n2 = int(input("Introduce un numero"))
    n3 = int(input("Introduce un numero"))

    if n1 >= n2 and n1 >=n3:
        maximo = n1
        
def hoja2_ej6():
    number = int(input("Introduce an integer: "))
    while number != 0:
       decimal = number / 2 - int(number / 2)
       if number > 0:
           if decimal == 0:
               print("Your number is even.")
           else:
               print("Your number is odd.")
       number = int(input("Introduce an integer: "))

def hoja2_ej7():
    number = int(input("Introduce an integer: "))
    while 0<= numer and number > 100:
        number = int(input("Introduce an integer: "))
    for i in range (1, 10):
        multiplication = i * number
        print(f"{i} * {number} = {multiplication}")

def suma(x,y):
    resultado = x + y
    return resultado 
print(resultado) #esto da error porque la variable resultado esta solo dentro de la definicion
#podemos ejecutar el programa de la siguiente manera
print(suma(2,3))

def suma(x,y):
    x = 1
    y = 2
    resultado = x + y
    return resultado
#esta funcion va a dar siempre 3, independientemente de los números que metas

def suma(): #en este caso no tiene sentido tenerlo como parámetro
    x = float(input("blah blah blah"))
    y = float(input("blah blah blah"))
    resultado = x + y

#para especificar el type que quieres de tus parametros, sin embargo esto es solo una especificacion, pues puedes meter un string y tambien va a funcionar
def suma(x : float, y : float) -> float:
    #aqui se puede especificar como funciona la función, son comentarios
    resultado = x + y
    return resultado

# 4/11/24

#mostrar elementos del 1 al 10

while i <= 10:
    i = 1
    print(i)
    i += 1
