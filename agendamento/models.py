from django.db import models

# Create your models here.
class agendamento(models.Model):
 
    dia = models.DateField(max_length=100)
    hora = models.DateField(max_length=100)
    local = models.CharField(max_length=100)



def __date__(self):
    return self.dia
    
def __date__(self):
    return self.hora

def __str__(self):
    return self.local

