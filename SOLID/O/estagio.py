from renumeravel import Renumeravel

class Estagio(Renumeravel):
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario;

    def renumerar(self) -> float:
        return self.salario
