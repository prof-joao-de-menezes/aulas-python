class Animal:
    def __init__(self, nome, idade, nivel_fome):
        self.__nome = nome
        self.__idade = idade
        self.__nivel_fome = nivel_fome

    @property
    def nome(self):
        return self.__nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade < 0:
            "idade invalida"
        else:
            self.__idade = nova_idade

    @property
    def nivel_fome(self):
        return self.__nivel_fome

    @nivel_fome.setter
    def nivel_fome(self, nivel_fome):
        self.__nivel_fome = nivel_fome