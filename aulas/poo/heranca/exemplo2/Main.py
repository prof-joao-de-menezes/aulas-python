# importam MÓDULOS
from Gato import Gato
from Cachorro import Cachorro
# ANIMAL -> Gato, Cachorro
class Main: # PRINCIPAL -> Somente executa códigos e cria objetos
    print("INICIANDO CLASSE PRINCIPAL")

    gato1 = Gato(2, "Tom", "Brasil")
    gato1.comer()
    gato1.dormir()
    gato1.mostrarIdade()
    gato1.cospePelo()
    print(gato1.nome)

    cachorro1 = Cachorro(3, "Zeus", "Alemanha")
    cachorro1.comer()
    cachorro1.dormir()
    cachorro1.mostrarIdade()
    cachorro1.latir()