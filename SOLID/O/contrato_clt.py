from renumeravel import Renumeravel

class ContratoCLT(Renumeravel):
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

    def renumerar(self) -> float:
        return self.salario - (self.salario * 0.1)