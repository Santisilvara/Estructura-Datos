class Vehiculo:

    marca: str
    combustible: str

    def __init__(self, marca, combustible):
        self.marca = marca 
        self.combustible = combustible

    def encender(self):
        pass

    def arrancar(self):
        pass

    def __str__(self):
        return "El vehiculo {} necesita gasolina {} para operar".format(self.marca, self.combustible)


class Moto(Vehiculo):
    pass 

class Carro(Vehiculo):
    pass


carro = Carro('Mazda', 'Extra')
print(carro)

moto = Moto('Suzuki', 'Corriente')
print(moto)