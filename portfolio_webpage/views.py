from portfolio.settings import LANGUAGE_CODE
from django.http.response import BadHeaderError
from django.shortcuts import render, redirect
from portfolio_webpage.forms import ContactForm
from portfolio_webpage.utils import Email, send_email
# Create your views here.


def index(request):
    english = True

    if (request.LANGUAGE_CODE == "es"):
        english = False
    
    context = {
        'form': ContactForm(),
        'english': english
    }
    language = request.LANGUAGE_CODE
    return render(request, 'portfolio/index.html', context)


def succeed(request):
    context = {
        'message': 'Thank you for reaching out (:'
    }
    return render(request, 'portfolio/contact.html', context)


def oops(request):
    context = {
        'message': 'Uhhh this is awkward. Something went wrong, sorry. Try that later (:'
    }
    return render(request, 'portfolio/contact.html', context)


def send(request):  # I could call a function with all of this process from somewhere else, but its a small code anyways
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            send_email(form)

        else:
            return redirect('oops')

    return redirect('succeed')
