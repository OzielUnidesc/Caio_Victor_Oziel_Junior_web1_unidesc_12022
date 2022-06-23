from django.db import models

# Create your models here.
class aviso(models.Model):
 
    matricula_avi = models.IntegerField(max_length=100)
    assunto_avi = models.CharField(max_length=100)
    data_avi = models.DateField(max_length=100)



def __int__(self):
    return self.matricula_avi
    
def __str__(self):
    return self.assunto_avi

def __date__(self):
    return self.data_avi

