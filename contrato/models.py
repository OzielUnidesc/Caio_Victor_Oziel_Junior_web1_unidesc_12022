from django.db import models

# Create your models here.
class contrato(models.Model):
 
    dadosCliente = models.CharField(max_length=100)
    dadosCorretor = models.CharField(max_length=100)
    descricaoImovel = models.CharField(max_length=100)
    valor = models.IntegerField(max_length=100)
    documentacao = models.DateField(max_length=100)
    clausulaPenal= models.CharField(max_length=100)
   


def __str__(self):
    return self.dadosCliente
    
def __str__(self):
    return self.dadosCorretor

def __str__(self):
    return self.descricaoImovel

def __int__(self):
    return self.valor

def __date__(self):
    return self.documentacao

def __str__(self):
    return self.clausulaPenal

