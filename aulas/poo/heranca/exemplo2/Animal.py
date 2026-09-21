# CLASSE PAI
class Animal(object):
    def __init__(self, tipo, idade, regiao):
        self.tipo = tipo
        self.idade = idade
        self.regiao = regiao

    def comer(self):
        print(f"O animal {self.tipo} está comendo.")

    def dormir(self):
        print(f"O animal {self.tipo} está dormindo...")

    def mostrarIdade(self):
        print(f"O animal {self.tipo} tem {self.idade} anos de idade")