from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_welcome_email(user_email, username):
    subject = 'Добре дошли в Разкази от кутията със сармички!'
    message = f'Здравей, {username}! Радваме се, че се присъедини към нашите разказвачи на истории.'
    email_from = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user_email]

    send_mail(subject, message, email_from, recipient_list)