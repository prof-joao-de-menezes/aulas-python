class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Pedido:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        try:
            for item in self.produtos:
                print(item.nome, item.valor)
        except Exception as erro:
            print(f"Erro inesperado: {erro}")
        finally:
            print("Finalizando execução do método")

produto1 = Produto("Liquidificador", 100.00)
produto2 = Produto("Geladeira", 2500.00)
produto3 = Produto("Cama Casal", 1500.00)

pedido1 = Pedido()
# composição
pedido1.adicionar_produto(produto1)
pedido1.adicionar_produto(produto2)
pedido1.adicionar_produto(produto3)

pedido1.listar_produtos() # erro de execução

# vai continuar executando
print("Executando depois do método")
for produto in pedido1.produtos:
    print(produto.nome, produto.preco)

