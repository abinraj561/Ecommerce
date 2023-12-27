import smtplib
from email.mime.text import MIMEText
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import *
 
@receiver(post_save, sender=Customer)
def send_registration_email(sender, instance, created, **kwargs):
    
    if created:  
        sender_email = "admin@gmail.com"
        recipient_email = instance.email
        subject = "Welcome !!"
        body = f"Hello {instance.username},\n\nThank you for registering !"
 
        msg = MIMEText(body)
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
 
        smtp_server = 'smtp.mailtrap.io'
        smtp_port = 2525
        smtp_username = 'd7abdea92a45f3'
        smtp_password = '0b91f3fe63825f'
 
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
 
 
 