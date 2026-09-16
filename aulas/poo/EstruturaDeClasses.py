# POO -> Programação Orientada a Objetos

#toda classe precisa da palavra reservada class
class Aluno:# toda classe começa com letra maiúscula
    def __init__(self, nome, registro, notas): # metodo CONSTRUTOR
        #define a construção de um novo objeto
        #não se cria um objeto sem contrutor
        # nome = novo atributo da classe
        # nome_do_aluno = parâmetro
        self.nome = nome
        self.registro = registro
        self.notas = notas
        # todos os alunos, OBRIGATORIAMENTE precisam ter nome e registro

    def mostrarNomeAluno(self): # metodo que usa os valores de aluma instância
        # todos os metodos dentro de uma classe precisam de self
        # uso o self, pra pegar um valor dentro da classe
        print(self.nome)

    # metodo de formatação
    def __str__(self):
        return f"Nome: {self.nome}\nRegistro: {self.registro}\nNotas: {self.notas}\n"

#códigos fora da classe
#aluno1 = objeto
#quando eu faço a instância, eu insiro o valor no ATRIBUTO DO OBJETO
aluno1 = Aluno(
    "João",
    11111,
    [10,10,10,10]
)#instância nova -> objeto aluno1
aluno2 = aluno1 # criando um novo objeto, mas não cria instância nova
aluno3 = Aluno("Fulano", 22222, [5,8,9,6]) # outra instância
aluno4 = Aluno("Zezin", 0, [10,5,0,9])

# not compara valores None, ou que representam vazio
string = ""
numero_inteiro = 0
numero_quebrado = 0.0
lista = []
tupla = ()
boolean = False
vazio = None

if not aluno1.nome: # executa apenas quando encontra um valor vazio
    print("Aluno não tem valor registrado como nome.")

#acessando o metodo dentro da classe a partir de um objeto
# aluno1.mostrarNomeAluno()
# aluno2.mostrarNomeAluno()

todosOsAlunos = [aluno1, aluno2, aluno3, aluno4]

for aluno in todosOsAlunos:
    print(aluno)
