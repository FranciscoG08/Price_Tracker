import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

pass_Word = os.getenv("EMAIL_PASSWORD")
sender_Origin = os.getenv("EMAIL")

def send_email(msg):
    sender = sender_Origin
    password = pass_Word  # usar App Password do Gmail
    receiver = sender_Origin  # pode ser o mesmo
    
    message = MIMEText(msg)
    message["Subject"] = "Alerta de Preço"
    message["From"] = sender
    message["To"] = receiver
    
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender, password)
            server.send_message(message)
        print("Email enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")