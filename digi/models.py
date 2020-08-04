from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    message = models.TextField()


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username
