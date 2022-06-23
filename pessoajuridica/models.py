from django.db import models

# Create your models here.
class renovacao(models.Model):
    cnpj = models.CharField(max_length=100)
    razaoSocial = models.CharField(max_length=100)
    representanteLegal = models.CharField(max_length=100)

def __str__(self):
    return self.cnpj

def __str__(self):
    return self.razaoSocial

def __str__(self):
       return self.representanteLegal