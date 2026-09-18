class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
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

shampoo = Produto("Shampoo",
                  10.00,
                  50)

# PRIMEIRO TESTE OBRIGATÓIO
shampoo.__quantidade_estoque = -50
shampoo.__preco = -100

print(shampoo.__dict__)

shampoo.nome = "Nivea"
print(shampoo.__dict__)