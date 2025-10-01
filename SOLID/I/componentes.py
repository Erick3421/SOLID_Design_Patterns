from abc import ABC, abstractmethod

class Impressora(ABC):
    @abstractmethod
    def imprimir(self):
        pass

class Escanear(ABC):
    @abstractmethod
    def escanear(self):
        pass

class Fax(ABC):
    @abstractmethod
    def enviar_fax(self):
        pass