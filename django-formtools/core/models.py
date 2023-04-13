from django.db import models

# Create your models here.
class Pessoa(models.Model):
    """Pessoa"""
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

class Time(models.Model):
    """Time"""
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)

class Endereco(models.Model):
    """Endereço"""
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
