class Animal:
    def __init__(self, especie, nome):
        self.__especie = especie
        self.nome = nome

    def comer(self):
        print(f"O {self.nome} se alimentou")

    def descansar(self):
        print(f"O {self.nome} dormiu")

    def descricao(self):
        print(f"O {self.nome} é da especie {self.__especie}.")

class Cachorro(Animal):
    def __init__(self, especie, nome, raca):
        super().__init__(especie, nome)
        self.raca = raca

class Gato(Animal):
    def __init__(self, nome, raca):
        super().__init__("Gato", nome)
        self.raca = raca

class Main:
    gato = Gato("Max", "Siamês")
    cachorro = Cachorro("Cachorro", "Brutus", "Buldog")

    cachorro.descricao()
    cachorro.comer()

    gato.descricao()
    gato.comer()