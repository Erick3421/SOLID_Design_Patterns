from notificacao import NotificacaoService

class EmailService(NotificacaoService):
    def enviar(self, mensagem: str):
        print(f"Enviando email com a mensagem: {mensagem}")

class SMSService(NotificacaoService):
    def enviar(self, mensagem: str):
        print(f"Enviando SMS com a mensagem: {mensagem}")

class WhatsAppService(NotificacaoService):
    def enviar(self, mensagem: str):
        print(f"Enviando WhatsApp com a mensagem: {mensagem}")