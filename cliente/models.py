from django.db import models

# Create your models here.
class cliente(models.Model):
 
    dataCadastro = models.DateField(max_length=100)



def __date__(self):
    return self.dataCadastro
    
