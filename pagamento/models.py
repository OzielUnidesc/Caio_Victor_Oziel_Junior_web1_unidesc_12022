from django.db import models

# Create your models here.
class pagamento(models.Model):

    valor_pag = models.IntegerField(max_length=100)
    forma_pag = models.CharField(max_length=100)
    parcela_pag = models.IntegerField(max_length=100)
    data_pag = models.DateField(max_length=100)
    banco_pag = models.CharField(max_length=100)
    agencia_pag = models.CharField(max_length=100)
    conta_pag = models.CharField(max_length=100)

def __Int__(self):
    return self.valor_pag

def __str__(self):
    return self.forma_pag

def __int__(self):
       return self.parcela_pag

def __date__(self):
    return self.data_pag

def __str__(self):
    return self.banco_pag
    
def __str__(self):
    return self.agencia_pag

def __str__(self):
    return self.conta_pag