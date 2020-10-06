from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm
from .models import CustomUser


class CustomSignUpForm(SignupForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "placeholder": "First Name",
        'class': 'form-control',
        'label': 'form-label'
    }))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        "placeholder": "Last Name",
        'class': 'form-control',
        'label': 'form-label'
    }))

    class Meta:
        model = CustomUser
        fields = ('__all__')

    def signup(self, request, user):
        user.first_name = self.cleaned_data.get['first_name']
        user.last_name = self.cleaned_data.get['last_name']
        user.save()


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


PROJECTCHOICE = [
    ('branding', "Branding"),
    ('copywriting', "Copywriting"),
    ('web developement', "Web Developement"),
    ('UI/UX Design', "UI/UX Design"),
]


class ProjectForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Full Name',
    }))
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={
        'class': "form-control",
        'placeholder': 'Your Email',
    }))
    phone = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Phone',
    }))
    company = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Company',
    }))
    budget = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': "form-control",
        'placeholder': 'Budget',
    }))
    project_type = forms.CharField(max_length=100, widget=forms.Select(choices=PROJECTCHOICE,  attrs={
        'class': "service-select",
        'placeholder': 'Project Type',
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': "service-textarea",
        'placeholder': 'Budget',
    }))
