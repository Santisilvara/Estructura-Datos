import pandas as pd

class Cultura:
    referencia = str
    nombre = str
    suma = float
    edades = float
    promedio = float 

    def __init__(self, referencia, nombre, año):
        self.referencia = referencia
        self.nombre = nombre
        self.año = año
        self.df = None
    
    def leer_archivo(self):
        #Con esto se lee el archivo seleccionado
        url = self.referencia
        self.df = pd.read_csv(url, sep=";")
        self.suma_edades()
        

    def __str__(self): 
        return "El archivo de nombre: {}, y de url: {}".format(self.nombre,self.referencia)


    def suma_edades(self):
        #Con esto se hacen los calculos, se suman todas las edades y se da el total
        if self.año in [2017,2019]:
            self.suma = sum(self.df.annos)
            print("La suma de edades de todas las personas es de: ", self.suma)
            self.promedio_edades()
        else:
            self.suma = sum(self.df.años)
            print("La suma de edades de todas las personas es de: ", self.suma)
            self.promedio_edades()
    
    def promedio_edades(self):
        #Con esto se hace el calculo de promedio de las edades con el total
        if self.año in [2017,2019]:
            self.edades = len(self.df.annos)
            self.promedio = (self.suma/self.edades)
            print("El promedio de edad en el censo: ", self.promedio)
            print("-"*40)

#Diccionario con las urls de los archivos .csv de cada año
urls = {
    2009 : "http://medata.gov.co/sites/default/files/medata_harvest_files/encuesta_cultura_2009.csv",
    2011 : "http://medata.gov.co/sites/default/files/medata_harvest_files/encuesta_cultura_2011.csv",
    2013 : "http://medata.gov.co/sites/default/files/medata_harvest_files/encuesta_cultura_2013.csv",
    2015 : "http://medata.gov.co/sites/default/files/medata_harvest_files/encuesta_cultura_2015.csv",
    2017 : "http://medata.gov.co/sites/default/files/medata_harvest_files/encuesta_cultura_2017.csv",
    2019 : "http://medata.gov.co/sites/default/files/medata_harvest_files/encuesta_cultura_2019.csv"
    
}
def comienzo():
    #Con esto se le da inicio al programa, y permite que el usuario elija el año preferido
    print("Con esto se puede leer el promedio de edad y la suma de todas las edades de los censados de las encuestas de cultura de los años seleccionados")
    while True:
        año = int(input("Digite el año que desea conocer (solo 2009,2011,2013,2015,2017 y 2019): "))
        if año in [2009, 2011, 2013, 2015, 2017, 2019]:
            cultura = Cultura(urls[año], "Censo de cultura del año {}".format(año),año )
            print(cultura)
            cultura.leer_archivo()
            break
        else:
            print("No selecciono un año permitido, ingreselo de nuevo")

#Inicio del programa
comienzo()


