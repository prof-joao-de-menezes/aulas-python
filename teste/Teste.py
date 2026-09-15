from aulas.Funcoes import Nome

class Funcionario: # criar uma nova classe
    nome = "João"  # atributo -> dentro de classe

# FORA DA CLASSE
nome = "Felipe" # variável -> fora de classe

print(nome) # Variável normal
print(Funcionario.nome) # INSTÂNCIA
print(Nome.nome) # INSTÂNCIA