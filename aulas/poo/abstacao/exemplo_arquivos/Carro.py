from Veiculo import Veiculo

class Carro(Veiculo):
    def acelerar(self):
        print("Carro acelerando")

    def dar_grau(self):
        print("Carro NÃO CONSEGUE dar grau")

if __name__ == "__main__":
    carro1 = Carro()
    carro1.acelerar()