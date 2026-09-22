# importam MÓDULOS
from Gato import Gato
from Cachorro import Cachorro
from CachorroDomestico import CachorroDomestico
from Animal import Animal
from aulas.poo.heranca.exemplo2.Baleia import Baleia


# ANIMAL -> Gato, Cachorro
class Main: # PRINCIPAL -> Somente executa códigos e cria objetos
    print("INICIANDO CLASSE PRINCIPAL")

    gato1 = Gato(2, "Tom", "Brasil", "Carnivoro")
    gato1.comer()
    gato1.dormir()
    gato1.mostrarIdadeDoGato()
    gato1.cospePelo()
    gato1.alimentando()

    cachorro1 = Cachorro(3, "Zeus", "Alemanha")
    cachorro1.comer()
    cachorro1.dormir()
    cachorro1.mostrarIdade()
    cachorro1.latir()
    cachorro1.aniversario()

    cachorro_domestico = CachorroDomestico
    cachorro_domestico.nome = "Max"
    print(f"O nome do seu cachorro deméstico é: {cachorro_domestico.nome}")
    cachorro_domestico.tipo = "Pug"
    print(f"A raça do cachorro é {cachorro_domestico.tipo}")

    # NÃO DEVO INSTANCIAR CLASSE PAI
    girafa = Animal("Girafa", 12, "Japão")
    girafa.comer()
    girafa.dormir()
    girafa.mostrarIdade()

    # CORRETO
    baleia = Baleia("Baleia", 12, "Oceano")
    baleia.comer()
    baleia.dormir()







