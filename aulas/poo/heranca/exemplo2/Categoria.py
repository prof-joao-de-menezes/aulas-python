class Categoria:
    def __init__(self, cadeiaAlimentar):
        self.cadeiaAlimentar = cadeiaAlimentar

    def alimentando(self):
        print(f"Esse animal é {self.cadeiaAlimentar}")