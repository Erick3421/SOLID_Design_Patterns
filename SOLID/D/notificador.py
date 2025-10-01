from notificacao import NotificacaoService

class Notificador:
    def __init__(self, notificador: NotificacaoService):
        self.notificador = notificador

    def notificar(self, mensagem: str):
        self.notificador.enviar(mensagem)