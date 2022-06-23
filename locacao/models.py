from django.db import models

# Create your models here.
class locacao(models.Model):
 
    dataDesocupacao = models.DateField(max_length=100)
    periodo = models.DateField(max_length=100)
    formaGarantia = models.CharField(max_length=100)
    fiador = models.CharField(max_length=100)


def __date__(self):
    return self.dataDesocupacao
    
def __date__(self):
    return self.periodo

def __str__(self):
    return self.formaGarantia

def __str__(self):
    return self.fiador
