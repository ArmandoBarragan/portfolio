from django import forms

class ContactForm(forms.Form):
    sender_email = forms.EmailField()
    name = forms.CharField(max_length=50)
    message = forms.CharField(max_length=300)
