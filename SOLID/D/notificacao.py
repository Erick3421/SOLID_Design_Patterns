from abc import ABC, abstractmethod

class NotificacaoService(ABC):
    @abstractmethod
    def enviar(self, mensagem: str):
        pass