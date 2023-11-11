import requests
from bs4 import BeautifulSoup

class Nodo:
    def __init__(self, datos):
        self.datos = datos
        self.anterior = None
        self.siguiente = None
        self.id = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.ultimo_id = 0 

    def agregar(self, datos):
        nuevo_nodo = Nodo(datos)
        self.ultimo_id += 1
        nuevo_nodo.id = self.ultimo_id  
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(f"ID: {actual.id}")
            for clave, valor in actual.datos.items():
                print(f"{clave}: {valor}")
            print()  
            actual = actual.siguiente

    def obtener_por_id(self, id_busqueda):
        actual = self.cabeza
        while actual:
            if actual.id == id_busqueda:
                return actual
            actual = actual.siguiente
        return None


url = 'https://www.alkomprar.com/computadores-tablet/computadores-portatiles/c/BI_104'
respuesta = requests.get(url)

soup = BeautifulSoup(respuesta.text, 'html.parser')

lista_datos = ListaDoblementeEnlazada()

contenedores_celular = soup.find_all('div', class_='dynamic-carousel__item-container')

for contenedor in contenedores_celular:
    elemento_nombre = contenedor.find('h3', class_='dynamic-carousel__title')
    elemento_precio = contenedor.find('span', class_='dynamic-carousel__price').find('span')
    elemento_imagen = contenedor.find('img', class_='dynamic-carousel__img')['data-src']
    elemento_enlace = contenedor.find('a', class_='splinter-link')['href']

    if elemento_nombre and elemento_precio and elemento_imagen and elemento_enlace:
        nombre = elemento_nombre.text.strip()
        precio = elemento_precio.text.strip()
        enlace = elemento_enlace
        imagen_url = elemento_imagen


        datos_celular = {
            'Nombre': nombre,
            'Precio': precio,
            'Imagen': imagen_url,
            'Enlace': enlace,
        }

        lista_datos.agregar(datos_celular)

print("Datos almacenados en la lista doblemente enlazada:")
lista_datos.mostrar()