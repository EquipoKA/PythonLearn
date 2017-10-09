#! /usr/bin/python3

def triangulo(numero=1,lado=10, caracter='*'):
    for j in range (0, numero):
        for i in range (0, lado + 1):
            print (caracter * i)
        for i in range (lado, 0, -1):
            print(caracter * i)


triangulo(lado=5)