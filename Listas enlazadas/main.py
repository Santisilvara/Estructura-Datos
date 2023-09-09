import random
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
class ListaEnlazada:
    def __init__(self):
        self.primero = None
    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.primero:
            self.primero = nuevo_nodo
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    
    def crear_lista_recursiva(self, num_nodos):
        if num_nodos <= 0:
            return
        nuevo_dato = random.randint(1, 10)
        self.insertar(nuevo_dato)
        self.crear_lista_recursiva(num_nodos - 1)
    
    def imprimir_lista(self):
        actual = self.primero
        numero_nodo = 1  
        while actual:
            print(f"El Nodo {numero_nodo} tiene un dato de valor: {actual.dato}")
            actual = actual.siguiente
            numero_nodo += 1
num_nodos_deseados = int(input("Indique el número de nodos que desea hacer: "))
mi_lista = ListaEnlazada()
mi_lista.crear_lista_recursiva(num_nodos_deseados)
mi_lista.imprimir_lista()
