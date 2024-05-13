import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email(destinatario, assunto, mensagem):
    """
    Envia um e-mail simples para o destinatário especificado.

    Args:
        destinatario (str): O endereço de e-mail do destinatário.
        assunto (str): O assunto do e-mail.
        mensagem (str): O corpo da mensagem do e-mail.
    """
    # Configurações de conexão com o servidor SMTP
    smtp_server = 'smtp.example.com'
    smtp_port = 587  # Porta de envio do servidor SMTP
    smtp_user = 'pedrolarrieudev@gmail.com'  # Configura seu e-mail
    smtp_password = 'Incorreta1'  # Sua senha

    # Iniciando conexão com o servidor SMTP
    server = None
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Habilita criptografia TLS
        server.login(smtp_user, smtp_password)  # Login no servidor SMTP

        # Construir mensagem de e-mail
        msg = MIMEMultipart()
        msg['From'] = smtp_user
        msg['To'] = destinatario
        msg['Subject'] = assunto

        # Adicionando o corpo da mensagem
        msg.attach(MIMEText(mensagem, 'plain'))

        # Envia e-mail
        server.sendmail(smtp_user, destinatario, msg.as_string())
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print("Erro ao enviar e-mail:", str(e))
    finally:
        if server:
            # Fecha conexão com o servidor SMTP
            server.quit()

# Exemplo de uso:
destinatario = 'destinatario@example.com'
assunto = 'Assunto do e-mail'
mensagem = 'Corpo da mensagem do e-mail'
enviar_email(destinatario, assunto, mensagem)
