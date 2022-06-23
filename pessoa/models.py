from django.db import models

# Create your models here.
class pessoafisica(models.Model):

    matricula = models.IntegerField(max_length=100)
    telefone = models.CharField(max_length=100)
    cep = models.CharField(max_length=100)
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=100)

def __Int__(self):
    return self.matricula

def __str__(self):
    return self.telefone

def __str__(self):
       return self.cep

def __str__(self):
    return self.rua

def __str__(self):
    return self.bairro
    
def __str__(self):
    return self.cidade

def __str__(self):
    return self.uf

