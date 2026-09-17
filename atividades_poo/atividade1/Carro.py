class Carro:
    def __init__(self, dono, cor, tipo, modelo, ano, fabricante):
        self.__dono = dono # Privado -> _Carro__dono
        self.cor = cor # Pública
        self.tipo = tipo
        self.modelo = modelo
        self.ano = ano
        self.fabricante = fabricante

    def __str__(self):
        return (f"Informações do carro:"
                f"\n\tDono (valor classe): {self._Carro__dono}"
                f"\n\tCor: {self.cor}"
                f"\n\tTipo: {self.tipo}"
                f"\n\tModelo: {self.modelo}"
                f"\n\tAno: {self.ano}"
                f"\n\tFabricante: {self.fabricante}")

    def acelerar(self): # retorna um valor
        print(f"O {self.__dono} acelerou o {self.modelo}")

    def frear(self): # metodos sem return, são vazios
        print("O carro freiou")

    def buzinar(self):
        print("O carro buzinou")

#lado de fora da Classe
carro_gustavo = Carro(
    "Gustavo",
    "Vermelho",
    "Popular",
    "Fiesta",
    2016,
    "Ford"
)

carro_vinicius = Carro("Vinicius","Amarelo", "Popular", "Camaro", 2025, "GM")

# carro_victor = Carro(input("Qual seu nome: "),
#                      input("Qual a cor do seu carro: "),
#                      input("Qual o tipo do carro: "),
#                      input("Qual o modelo do carro: "),
#                      int(input("Qual o ano do carro: ")),
#                      input("Qual o fabricante do carro: "))

carro_victor = Carro("Victor", "Azul", "Popular", "BYD", 2025, "GM")
carro_victor.dono = "João"
print(carro_victor.dono)
carro_victor.__dono = "Felipe"
print(carro_victor.__dono)

print(carro_victor._Carro__dono)