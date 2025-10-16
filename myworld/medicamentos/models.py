from django.db import models



class DepositoAmpollas(models.Model):
 
  id = models.AutoField(primary_key=True)  
  nombreMedicamento = models.CharField(max_length=255)
  cantidadStock = models.IntegerField(max_length=255)
  cantDispensada= models.IntegerField(max_length=255)
  cantIngresada=models.IntegerField(max_length=255)
# Create your models here.
