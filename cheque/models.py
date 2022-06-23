from django.db import models

# Create your models here.
class cheque(models.Model):
 
    financeiro = models.CharField(max_length=100)
    nomeCliente = models.CharField(max_length=100)
    numero = models.CharField(max_length=100)
    dataAbertura = models.DateField(max_length=100)



def __str__(self):
    return self.financeiro
    
def __str__(self):
    return self.nomeCliente

def __str__(self):
    return self.numero

def __date__(self):
    return self.dataAbertura

