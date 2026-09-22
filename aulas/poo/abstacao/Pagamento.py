from abc import ABC, abstractmethod
# Abstract Base Class

# classe PAI
# DEFINIR INTERFACE
class Pagamento(ABC): # Classe ABSTRATA
    @abstractmethod
    def pagar(self, valor: float): # metodo ABSTRATO
        # Defino a INTERFACE
        # NÃO defino sua IMPLEMENETAÇÃO
        pass

    def amortizar(self, parcela, metodo): # metodos CONCRETOS
        print(f"Amortizando a {parcela}º parcela via {metodo}.")

# classe FILHA
# DEFINO INTERFACE
class Pix(Pagamento):
    def pagar(self, valor): # sobreescrita
        print("Desconto de 10% no PIX")
        desconto = valor * 0.10
        print(f"Pagando R${(valor - desconto):.2f} via PIX")
        # Defino a IMPLEMENTAÇÃO do metodo Herdado

#DEFINO INTERFACE
class Boleto(Pagamento):
    def pagar(self, valor):
        print(f"Pagando R${valor} via BOLETO")

#DEFINO INTERFACE
class Cartao(Pagamento):
    def pagar(self, valor):
        print(f"Pagando R${valor} no debido via CARTAO")

    def parcelar(self, valor):
        print(f"Pagando R${valor} parcelado via CARTAO")

# DEFINO AS IMPLEMENTAÇÕES
class Principal:
    #                           classe(Pagamento)   float
    def efetuar_pagamento(self, Pagamento, valor):
        print(f"Efetuando pagamento")
        Pagamento.pagar(valor)
        print("Pagamento efetuado com sucesso!")

    print("====== EFETUANDO PAGAMENTOS ======")
    efetuar_pagamento(Pix(), 100.00)