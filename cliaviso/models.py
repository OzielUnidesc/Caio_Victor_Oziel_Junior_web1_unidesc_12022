from django.db import models

# Create your models here.
class cliaviso(models.Model):
 
    mensagem = models.CharField(max_length=100)



def __str__(self):
    return self.mensagem
    
