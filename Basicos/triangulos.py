#! /usr/bin/python3

def triangulo(lado=10, caracter='*'):
    for i in range (0, lado + 1):
        print (caracter * i)
    for i in range (lado, 0, -1):
        print(caracter * i)

triangulo()