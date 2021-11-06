nombre = "Rodrigo"
apellido = "Bravo"
edad = 28
a=4
b=30


def sumar(a,b):
    resultado=a+b
    print(resultado)
    return resultado

def presentarse():
    saludo = "Hola ", nombre, " ", apellido, " .Tenes ", edad
    print(saludo)
    return saludo