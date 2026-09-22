# CLASSE PAI
class Animal():
    def __init__(self, tipo, idade, regiao):
        self._tipo = tipo # protected
        self.__idade = idade # private
        self._regiao = regiao # protected

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def regiao(self):
        return self._regiao

    def comer(self): # publicos
        print(f"O animal {self._tipo} está comendo.")

    def dormir(self):# publicos
        print(f"O animal {self._tipo} está dormindo...")

    def mostrarIdade(self):# publicos
        print(f"O animal {self._tipo} tem {self.__idade} anos de idade")