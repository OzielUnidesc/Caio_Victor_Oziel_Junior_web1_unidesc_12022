from socket import TIPC_LOW_IMPORTANCE
from django.db import models

# Create your models here.
class imovel(models.Model):
 
    matricula_imo = models.IntegerField(max_length=100)
    rua_imo = models.CharField(max_length=100)
    cep_imo = models.CharField(max_length=100)
    bairro_imo = models.CharField(max_length=100)
    cidade_imo = models.CharField(max_length=100)
    uf_imo = models.CharField(max_length=100)
    tamanho_imo = models.CharField(max_length=100)
    comodos_imo = models.CharField(max_length=100)
    garagem_imo = models.CharField(max_length=100)
    valor_imo = models.IntegerField(max_length=100)
    tipo_imo = models.CharField(max_length=100)
    status_imo = models.CharField(max_length=100)

def __int__(self):
    return self.matricula_imo
    
def __str__(self):
    return self.rua_imo

def __str__(self):
    return self.cep_imo

def __str__(self):
    return self.bairro_imo
    
def __str__(self):
    return self.cidade_imo

def __str__(self):
    return self.uf_imo

def __str__(self):
    return self.tamanho_imo
    
def __str__(self):
    return self.comodos_imo

def __str__(self):
    return self.garagem_imo

def __int__(self):
    return self.valor_imo
    
def __str__(self):
    return self.status_imo

def __str__(self):
    return self.tipo_imo