from servicos import EmailService, SMSService, WhatsAppService
from notificador import Notificador

email_notificador = Notificador(EmailService())
sms_notificador = Notificador(SMSService())
whatsapp_notificador = Notificador(WhatsAppService())

email_notificador.notificar("Bem-vindo ao sistema!")
sms_notificador.notificar("Seu código é 123456")
whatsapp_notificador.notificar("Sua entrega chegou 🚚")