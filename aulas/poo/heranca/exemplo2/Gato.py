# CLASSE FILHA
#    arquivo.py    classe
from Animal import Animal
from Categoria import Categoria


class Gato(Animal, Categoria): # rehança multipla
    def __init__(self, idade, nome, regiao, cadeiaAlimentar):
        super().__init__(idade = idade, tipo = "Gato", regiao = regiao)# super -> acessa casse pai
        self.nome = nome
        self.cadeiaAlimentar = cadeiaAlimentar
        

    def cospePelo(self):
        print(f"O gato {self.nome} cospiu pelo...")

    def mostrarIdadeDoGato(self):
        print(self._tipo)