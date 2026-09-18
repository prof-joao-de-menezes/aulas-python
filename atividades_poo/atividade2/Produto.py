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

shampoo = Produto("Shampoo",
                  10.00,
                  50)

# PRIMEIRO TESTE OBRIGATÓIO
shampoo.__quantidade_estoque = -50
shampoo.__preco = -100

print(shampoo.__dict__)