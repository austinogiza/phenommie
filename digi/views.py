from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Contact
from .forms import ContactForm

# Create your views here.


def home(request):
    return render(request, 'index.html')


def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")

        contact = Contact(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        contact.save()
        return redirect('digi:contactsuccess')

    context = {
        'form': form
    }

    return render(request, 'contact.html', context)


def contactsuccess(request):
    return render(request, 'contact-success.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def service(request):
    return render(request, 'services.html')


def courses(request):
    return render(request, 'courses.html')
