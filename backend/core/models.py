from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class Usuario(AbstractUser):
    nome = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)


class Boletos(models.Model):
    titular = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    pago = models.BooleanField(default=False)
    data = models.DateTimeField(auto_now=True)
