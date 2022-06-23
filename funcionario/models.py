from django.db import models

# Create your models here.
class funcionario(models.Model):
 
    cpf = models.CharField(max_length=100)
    rg = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    dataNascimento = models.DateField(max_length=100)
    carteiraTrabalho = models.CharField(max_length=100)
    salario = models.IntegerField(max_length=100)
    pis = models.CharField(max_length=100)


def __str__(self):
    return self.cpf
    
def __str__(self):
    return self.rg

def __str__(self):
    return self.nome

def __str__(self):
    return self.sexo

def __date__(self):
    return self.dataNascimento

def __str__(self):
    return self.carteiraTrabalho

def __str__(self):
    return self.salario

def __str__(self):
    return self.pis