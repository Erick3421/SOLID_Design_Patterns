from componentes import Impressora, Escanear, Fax

class ImpressoraSimples:
    def imprimir(self):
        print("Imprimindo...")


class ImpressoraMultifuncional(Impressora,Escanear,Fax):
    def imprimir(self):
        print("Imprimindo documento...")

    def escanear(self):
        print("Escaneando documento...")

    def enviar_fax(self):
        print("Enviando fax...")