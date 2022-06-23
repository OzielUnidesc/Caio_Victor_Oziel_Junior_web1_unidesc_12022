from django.db import models

# Create your models here.
class renovacao(models.Model):
    dataDesocupacao = models.DateField(max_length=8)
    dataRenovacao = models.DateField(max_length=8)
    cartorio = models.CharField(max_length=100)

def __date__(self):
    return self.dataDesocupacao

def __date__(self):
    return self.dataRenovacao

def __str__(self):
       return self.cartorio