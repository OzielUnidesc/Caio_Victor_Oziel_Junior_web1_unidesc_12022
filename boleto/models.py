from django.db import models

# Create your models here.
class boleto(models.Model):
 
    codCliente = models.CharField(max_length=100)
    nomeCliente = models.CharField(max_length=100)



def __str__(self):
    return self.codCliente
    
def __str__(self):
    return self.nomeCliente

