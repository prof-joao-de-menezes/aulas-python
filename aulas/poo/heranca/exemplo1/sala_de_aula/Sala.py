from aulas.poo.heranca.exemplo1.diretoria.Coordenacao import Coordenacao

class Sala(Coordenacao):
    def __init__(self, laboratorio, tipo, professores, cursos, alunos):
        super().__init__(professores[0], cursos, alunos)
        self.__laboratorio = laboratorio
        self.__tipo = tipo

    def ter_aula(self):
        print(f"Aula de: {self.cursos}"
              f" no laboratório de {self.__tipo}"
              f"\n Com o professor: {self.escolher_professores(0)}"
              f"\n Com os alunos:")
        for aluno in self.alunos:
            print(aluno)


sala_1 = Sala("Lab 7",
              "Tecnologia",
              "João",
              "Python",
              ["Fulano", "Beltrano", "Ciclano"])

sala_1.ter_aula()


