from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.hashers import make_password, check_password


class CustomUser(AbstractBaseUser):
    telefone = models.CharField(max_length=11, null=True, blank=True)
    endereco = models.TextField(null=True, blank=True)

class RegistroCalendario(models.Model):
    nome = models.CharField(max_length=100),
    tipo = models.CharField(max_length=50),
    dia_hora = models.DateTimeField(),
    alerta = models.DateTimeField(),
    status = models.BooleanField(default=False),
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class Usuario(models.Model):
    nomeUsur =  models.CharField(max_length=100),
    emailUser = models.EmailField(max_length=254),
    senha = models.CharField(max_length=128)