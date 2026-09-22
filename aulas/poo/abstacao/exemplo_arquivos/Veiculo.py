from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def acelerar(self): # metodo que EXIGE sobreescrita
        pass

    def dar_grau(self):
        print("Dando grau e tomando multa")