class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque

    def adicinar_estoque(self, quantidade):
        if quantidade > 0:
            self.__quantidade_estoque += quantidade
        else:
            print("Erro: quantidade inválida.")

objeto_produto = Produto("Shampoo",
                         10.00,
                         50)
print(objeto_produto.__dict__)
objeto_produto.adicinar_estoque(-100)
print(objeto_produto.__dict__)