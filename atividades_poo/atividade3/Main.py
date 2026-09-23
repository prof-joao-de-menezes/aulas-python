from Ave import Ave
from atividades_poo.atividade3.Mamifero import Mamifero

# Instanciando os animais
leao = Mamifero(nome="Simba", idade=5, nivel_fome=70, velocidade_kmh=80)
gaviao = Ave(nome="Sky", idade=2, nivel_fome=75, envergadura_asas=120)

# 1. Tentativa de alteração direta dos atributos privados (Proteção do Encapsulamento)
leao.__nivel_fome = -999
leao.__idade = -10

# 2. Testando ações que alteram o estado interno via Herança e Encapsulamento
leao.correr()          # Fome sobe de 70 para 90
gaviao.voar()          # Fome sobe de 75 para 90 (Sucesso)
gaviao.voar()          # Fome está em 90 -> Deve exibir: "Voo negado: Sky está faminto demais para voar!"

# 3. Testando alimentação
leao.alimentar(50)     # Fome cai de 90 para 40
leao.alimentar(-10)    # Deve exibir: "Erro: Porção inválida"

# 4. Exibição final dos resumos
print("\n--- RESUMO DO MAMÍFERO ---")
leao.emitir_som()
leao.exibir_resumo()

print("\n--- RESUMO DA AVE ---")
gaviao.emitir_som()
gaviao.exibir_resumo()

