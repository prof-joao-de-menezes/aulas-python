from abc import (ABC, abstractmethod)

class Veiculo(ABC):
    @abstractmethod
    def acelerar(self):
        pass

class Carro(Veiculo):
    def acelerar(self):
        print('Carro acelerar')

class Moto(Veiculo):
    def acelerar(self):
        print('Moto acelerar')

class Lancha(Veiculo):
    def acelerar(self):
        print('Lancha acelerar')

moto = Moto()
carro = Carro()
lancha = Lancha()

lista_veiculos = [moto, carro, lancha]

# mesmo metodo, ações diferentes
for veiculo in lista_veiculos:
    veiculo.acelerar()