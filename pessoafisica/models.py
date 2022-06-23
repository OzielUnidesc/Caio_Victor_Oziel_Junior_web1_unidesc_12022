from django.db import models

# Create your models here.
class pessoafisica(models.Model):

    cpf = models.CharField(max_length=100)
    rg = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    dataNascimento = models.DateField(max_length=100)

def __str__(self):
    return self.cpf

def __str__(self):
    return self.rg

def __str__(self):
       return self.nome

def __str__(self):
    return self.sexo

def __Date__(self):
    return self.dataNascimento    
