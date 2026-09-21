class Loja: # classe pai
    def __init__(self, nome_loja):
        self.__nome_loja = nome_loja

    @property
    def nome_loja(self):
        return self.__nome_loja
    @nome_loja.setter
    def nome_loja(self, nome_loja):
        self.__nome_loja = nome_loja

# HERANÇA
class Produto(Loja): # classe filha
    def __init__(self, nome, preco, quantidade_estoque):
        super().__init__(nome_loja="Atacadão")
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco):
        self.__preco = novo_preco

    @property
    def quantidade_estoque(self):
        return self.__quantidade_estoque

    @quantidade_estoque.setter
    def quantidade_estoque(self, novo_quantidade_estoque):
        self.__quantidade_estoque = novo_quantidade_estoque

    def adicinar_estoque(self, quantidade):
        if quantidade > 0:
            self.__quantidade_estoque += quantidade
        else:
            print("Erro: quantidade inválida.")


class Comprador:
    def __init__(self, nome, produdo_comprado):
        self.__nome = nome
        self.__produdo_comprado = produdo_comprado

    compra = Produto("Shampoo",
                     30.00,
                     100)

    compra.nome_loja = "Açai atacadista"
    print(compra.__dict__)

    outra_compra = Produto("Carro",
                     300000.00,
                     1)
    outra_compra.nome_loja = "Honda"
    print(outra_compra.__dict__)