#Hacer la logica para elimnar un nodo interno 
import random

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.primero = None

    def vacia(self):
        return self.primero is None

    def apilar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.primero
        self.primero = nuevo_nodo

    def desapilar(self, dato):
        if self.vacia():
            return
        if self.primero.dato == dato:
            self.primero = self.primero.siguiente
        else:
            temp = self.primero
            while temp.siguiente is not None and temp.siguiente.dato != dato:
                temp = temp.siguiente
            
            if temp.siguiente is not None:
                temp.siguiente = temp.siguiente.siguiente
            else:
                print(f"No se encontró el nodo con dato {dato} en la pila.")

    def imprimir(self,num_nodos):
        temp = self.primero
        while temp is not None:
            print(f"El nodo {num_nodos} tiene un dato de valor: {temp.dato}")
            temp = temp.siguiente
            num_nodos -= 1

def generar_numeros_aleatorios(num_nodos):
    datos = [random.randint(1, 100) for _ in range(num_nodos)]
    return datos

pila = Pila()
num_nodos = int(input("Ingrese el número de nodos a crear: "))
if num_nodos == 0:
    print("Sin nodos, la lista queda vacia")
else:
    datos_aleatorios = generar_numeros_aleatorios(num_nodos)
    for dato in datos_aleatorios:
        pila.apilar(dato)
    print("Pila inicial:")
    pila.imprimir(num_nodos)
    dato_a_eliminar = int(input("Ingrese el dato del nodo a eliminar: "))
    pila.desapilar(dato_a_eliminar)
    print("Pila después de eliminar el nodo:")
    pila.imprimir(num_nodos-1)