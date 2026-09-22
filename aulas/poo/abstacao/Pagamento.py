# PRECISA IMPORTAR PARA CRIAR CLASSE ABSTRATA
from abc import ABC, abstractmethod
# ABC -> Abstract Base Class
# abstractmethod -> Anotação dentro de abc

# classe PAI -> Geralmente abstrata
# DEFINIR INTERFACE
class Pagamento(ABC): # Classe ABSTRATA
    @abstractmethod
    def pagar(self, valor): # metodo ABSTRATO
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
    #                                       classe     atributo
    def efetuar_pagamento(metodo_pagamento: Pagamento, valor: float):
        print(f"Efetuando pagamento...")
        metodo_pagamento.pagar(valor)
        print("Pagamento efetuado com sucesso!\n")

    print("====== EFETUANDO PAGAMENTOS ======")
    lista_pagamentos = [
        (Pix(), 250), # index 0 (Classe, atributo)
        (Cartao(), 100.00),
        (Boleto(), 5000.00)
    ]

    #       Classe       atributo
    for metodo_pagamento, valor in lista_pagamentos:
        efetuar_pagamento(metodo_pagamento, valor)


