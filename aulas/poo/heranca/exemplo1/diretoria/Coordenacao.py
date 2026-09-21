class Coordenacao: # Classe PAI
    def __init__(self, professores, cursos, alunos):
        self.__professores = ["João", "Max", "Mateus"]
        self.__cursos = cursos
        self.__alunos = alunos

    # LISTA DE GET
    @property
    def cursos(self):
        return self.__cursos
    @property
    def professores(self):
        return self.__professores
    @property
    def alunos(self):
        return self.__alunos

    def escolher_professores(self, index_professor):
        return self.__professores[index_professor]