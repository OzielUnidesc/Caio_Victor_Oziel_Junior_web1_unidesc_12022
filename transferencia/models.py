from django.db import models

# Create your models here.
class transferencia(models.Model):
    tipo = models.CharField(max_length=100)
    codidentificacao = models.CharField(max_length=100)

   
def __str__(self):
       return self.tipo
def __str__(self):
    return self.codidentificacao

   