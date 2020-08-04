from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={

        'placeholder': 'Your Name',
        'class': 'form-control',
        'label': 'form-label'
    }))

    email = forms.EmailField(max_length=100, required=True, widget=forms.TextInput(attrs={

        'placeholder': 'Your E-mail',
        'class': 'form-control',
        'label': 'form-label'
    }))
    subject = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={

        'placeholder': 'Your Subject',
        'class': 'form-control'
    }))

    message = forms.CharField(widget=forms.Textarea(attrs={

        'placeholder': 'Type Your Message',
        'class': 'form-textarea'
    }))
