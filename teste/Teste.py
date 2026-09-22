from abc import ABC

class Pagamento(ABC):
    def pagar(self, valor):
        pass


class Pix(Pagamento):
    def pagar(self, valor):
        print(f"Pagando {valor} via pix")


class Cartao(Pagamento):
    def pagar(self, valor):
        print(f"Pagando {valor} via cartão")

