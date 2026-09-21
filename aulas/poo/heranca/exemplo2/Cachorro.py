# CLASSE FILHA
from Animal import Animal

class Cachorro(Animal):
    def __init__(self, idade, nome, regiao):
        super().__init__(tipo = "Cachorro", idade = idade, regiao = regiao)
        self.nome = nome

    def latir(self):
        print(f"O {self.tipo} está latindo...")