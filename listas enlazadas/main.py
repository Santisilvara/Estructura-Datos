import random

class Nodo:

    dato = random.randint(0, 5)
    apuntador = None

class Lista_Enlazada:
    def __int__(self):
        self.cabeza = None
        











    def __init__(self, dato, apuntador):
        self.dato = dato
        self.apuntador = apuntador

    def __str__(self):
        return self.dato
