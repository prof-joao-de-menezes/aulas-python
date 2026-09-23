from Animal import Animal

class Mamifero(Animal):
    def __init__(self, nome, idade, nivel_fome, velocidade_kmh):
        super().__init__(nome, idade, nivel_fome)
        self.__velocidade_kmh = velocidade_kmh

    def correr(self):
        self.nivel_fome += 20
        print(f"{self.nome} correu a {self.__velocidade_kmh} km/h!")

    def emitir_som(self): # SOBREESCRITA
        print(f"{self.nome} ruge/ruge alto!")

    def exibir_resumo(self): # SOBREESCRITA
        super().exibir_resumo()
        print(f"Velocidade: {self.__velocidade_kmh} km/h!")