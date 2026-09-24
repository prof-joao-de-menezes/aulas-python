class Teste:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

obj = Teste("João")

obj._Teste__nome = "Felipe"

print(obj.__dict__)