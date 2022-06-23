from django.db import models

# Create your models here.
class pagamento(models.Model):
 
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    permissao = models.CharField(max_length=100)


def __str__(self):
    return self.email
    
def __str__(self):
    return self.senha

def __str__(self):
    return self.permissao