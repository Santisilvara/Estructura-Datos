class Vehiculo:

    marca = " "
    combustible = " "

    def __init__(self,combustible,marca):
        self.marca = marca
        self.combustible = combustible 

    def encender(self ):
        pass

    def arrancar(self ):
        pass

carro = Vehiculo("corriente","mazda")
print(carro.marca, carro.combustible)
