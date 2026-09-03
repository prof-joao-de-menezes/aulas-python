caixa = 12

quanti_macas = int(input("Colheu quantas maças? "))

macas_sobraram = quanti_macas % 12

quantidade_caixas = quanti_macas // 12

print("Foram usadas ", quantidade_caixas, " caixas.")
print("Vão sobrar: ",macas_sobraram," maçãs.")