from django.http.response import BadHeaderError
from django.shortcuts import render, redirect
from django.core.mail import send_mail

class Email:
    def __init__(self, data):
        self.name = data['name']
        self.subject = "Email del portafolio, por " + self.name
        self.sender_email = data['sender_email']
        self.message = data['message'] + '\n' + self.sender_email


def send_email(form):
    data = form.cleaned_data
    email = Email(data)

    if email.subject and email.message and email:
        try:
            send_mail(email.subject, email.message, email.sender_email, [
                'armandobp765@gmail.com'], fail_silently=False)

        except BadHeaderError:
            return redirect('oops')
