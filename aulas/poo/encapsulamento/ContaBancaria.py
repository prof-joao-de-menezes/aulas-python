class ContaBancaria: # nome da classe
    def __init__(self, titular, saldo): # metodo construtor
        self.titular = titular # self.atributo = valor do parametro
        self.__saldo = saldo # private

    # metodos Getters e Setters (Get = Pegar e Set = Inserir)
    def get_titular(self):
        senha = 1234
        senha_digitada = int(input('(GET) Digite sua senha: '))

        if senha == senha_digitada:
            return self.titular
        else:
            return 'Senha incorreta!'

    def set_titular(self, novo_titular):
        senha = 1234
        senha_digitada = int(input('(SET) Digite sua senha: '))

        if senha == senha_digitada:
            self.titular = novo_titular
            return 'Titular atualizada!'
        else:
            return 'Senha incorreta!'


conta_banco = ContaBancaria("João", 10000)
#print(conta_banco.titular) # Acesso diretamente o atributo
print(conta_banco.get_titular())

#conta_banco.titular = "Fulano" # modificando diretamente o atributo
conta_banco.set_titular("Ciclano") # modificando por metodo
print(conta_banco.get_titular())