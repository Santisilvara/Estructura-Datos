class Vehiculo:

    marca: str
    combustible: str
    tipo: str

    def __init__(self, marca, combustible):
        self.marca = marca 
        self.combustible = combustible

    def encender(self):
        pass
    
    def arrancar(self):
        pass

    def __str__(self):
        return "El vehiculo tipo {} {} necesita gasolina {} para operar".format(self.tipo, self.marca, self.combustible)


class Moto(Vehiculo):
  
    def __init__(self, marca, combustible):
        super().__init__(marca, combustible) 
        self.tipo = 'Moto'

class Carro(Vehiculo):
  
    def __init__(self, marca, combustible):
        super().__init__(marca, combustible) 
        self.tipo = 'Carro'


carro = Carro('Mazda', 'Extra')
print(carro)

moto = Moto('Suzuki', 'Corriente')
print(moto)