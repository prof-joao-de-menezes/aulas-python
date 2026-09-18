# FORMA CONVENCIONAL NÃO UTILIZADA NO PYTHON
class ContaBancaria: # nome da classe
    def __init__(self, titular, saldo): # metodo construtor
        self.titular = titular # self.atributo = valor do parametro
        self.__saldo = saldo # private

    # metodos Getters e Setters (Get = Pegar e Set = Inserir)
    # METODOS CONVENCIONAIS
    def get_titular(self):
        senha = 1234
        senha_digitada = int(input('(GET) Digite sua senha: '))

        if senha == senha_digitada:
            return self.titular
        else:
            return 'Senha incorreta!'

    def set_titular(self, novo_titular):
        self.__saldo = novo_titular

# conta_banco = ContaBancaria("João", 10000)
# #print(conta_banco.titular) # Acesso diretamente o atributo
# print(conta_banco.get_titular())
#
# #conta_banco.titular = "Fulano" # modificando diretamente o atributo
# conta_banco.set_titular("Ciclano") # modificando por metodo
# print(conta_banco.get_titular())

class ContaBancariaCorreta: # LÓGICA UTILIZADA NO PYTHON de get e set
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo # private

    @property # anotation -> anotação
    def saldo(self): # funciona como o GET
        return self.__saldo

    @saldo.setter # criando um SET novo no metodo
    # quando o usuário digitar objeto.saldo
    # acessa o metodo
    def saldo(self, novo_saldo): # funciona como o SET
        if novo_saldo < 0:
            print("Não é possivel colocar saldo negativo")
        else:
            self.__saldo = novo_saldo

    def sacar(self, valor_saque):
        if valor_saque <= self.__saldo:
            self.saldo -= valor_saque
            print(f'Quantidade retirada: {valor_saque}')
            print(f'Saldo restante: {self.saldo}')
        else:
            print(f'Saldo atual: {self.saldo}')
            print(f"Valor de saque {valor_saque}")
            print("Saldo insuficiente")

    def transferir(self, valor_transfer):
        if valor_transfer <= self.__saldo:
            print(f'Quantidade transferida: {valor_transfer}')
            self.saldo -= valor_transfer
        else:
            print(f'Saldo atual: {self.saldo}')
            print(f"Valor de transeferencia {valor_transfer}")
            print("Saldo insuficiente")
usuario_banco_correto = ContaBancariaCorreta("Jose", 500)
print("Saldo: ", usuario_banco_correto.saldo)

print("Adicinando fundos ao banco")
usuario_banco_correto.saldo = 5000
usuario_banco_correto.__saldo = -100000

print("Saldo: ", usuario_banco_correto.saldo)
usuario_banco_correto.sacar(1000)
print("Saldo: ", usuario_banco_correto.saldo)
usuario_banco_correto.transferir(1000)
print("Saldo: ", usuario_banco_correto.saldo)
usuario_banco_correto.transferir(10000)
print(usuario_banco_correto.__dict__)