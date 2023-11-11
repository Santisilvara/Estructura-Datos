from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np

class Nodo:
    def __init__(self, valor):
        self.dato = valor
        self.izquierda = None
        self.derecha = None

class Pila:
    def __init__(self):
        self.items = []

    def push(self, valor):
        self.items.append(valor)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.izquierda = self.cabeza
        self.cabeza = nuevo_nodo

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.dato:
            nodo.izquierda = self._insertar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.dato:
            nodo.derecha = self._insertar_recursivo(nodo.derecha, valor)
        return nodo

class Tarea:
    def __init__(self, descripcion, prioridad):
        self.descripcion = descripcion
        self.prioridad = prioridad

class TareasManager:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def entrenar_modelo(self):
        descripciones = [tarea.descripcion for tarea in self.tareas]
        prioridades = [tarea.prioridad for tarea in self.tareas]

        # Convertir las descripciones a características (por ejemplo, longitud de la descripción)
        caracteristicas = np.array([len(desc) for desc in descripciones]).reshape(-1, 1)

        # Dividir los datos en conjunto de entrenamiento y prueba
        X_train, X_test, y_train, y_test = train_test_split(caracteristicas, prioridades, test_size=0.2, random_state=42)

        # Entrenar el modelo de regresión lineal
        modelo = LinearRegression()
        modelo.fit(X_train, y_train)

        return modelo

    def predecir_prioridad(self, modelo, descripcion, limite_inferior=1, limite_superior=5):
        # Predecir la prioridad basada en la longitud de la descripción
        longitud_descripcion = len(descripcion)
        prioridad_predicha = modelo.predict([[longitud_descripcion]])[0]

        # Aplicar límites y convertir a entero
        prioridad_predicha = int(max(limite_inferior, min(limite_superior, prioridad_predicha)))
        return prioridad_predicha

# Programa principal
pila_tareas_pendientes = Pila()
pila_tareas_completadas = Pila()
lista_tareas = ListaEnlazada()
arbol_prioridades = ArbolBinario()
tareas_manager = TareasManager()

# Agregar tareas con descripciones y prioridades
tareas_manager.agregar_tarea(Tarea("Hacer la tarea de programación", 2))
tareas_manager.agregar_tarea(Tarea("Estudiar para el examen de estructuras de datos", 5))
tareas_manager.agregar_tarea(Tarea("Preparar presentación para el proyecto", 3))

# Entrenar el modelo
modelo_prioridades = tareas_manager.entrenar_modelo()

# Nueva tarea a predecir
nueva_tarea_descripcion = "Instalar el servicio web en el servidor"

# Predecir la prioridad
prioridad_predicha = tareas_manager.predecir_prioridad(modelo_prioridades, nueva_tarea_descripcion)

print(f"Prioridad predicha para '{nueva_tarea_descripcion}': {prioridad_predicha}")
