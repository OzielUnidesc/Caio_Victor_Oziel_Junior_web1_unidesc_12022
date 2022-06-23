from django.db import models

# Create your models here.
class corretor(models.Model):
 
    comissao = models.IntegerField(max_length=100)
    idCorretor = models.CharField(max_length=100)



def __int__(self):
    return self.comissao
    
def __str__(self):
    return self.idCorretor

