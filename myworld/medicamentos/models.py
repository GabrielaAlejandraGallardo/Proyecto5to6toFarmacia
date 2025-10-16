from django.db import models



class DepositoAmpollas(models.Model):
 
  idAmpolla = models.AutoField(primary_key=True)  
  nombreMedicamento = models.TextField(max_length=255)
  lote= models.CharField(max_length=255)
  vencimiento = models.DateField()  
  laboratorio = models.CharField(max_length=255)
  fecha= models.DateField()
  stockCritico = models.IntegerField(max_length=255)
  cantidadStock = models.IntegerField(max_length=255)
  cantDispensada= models.IntegerField(max_length=255)
  cantIngresada=models.IntegerField(max_length=255)
  SaldoMensual=models.IntegerField(max_length=255)
# Create your models here.
"""idAmpollas, descripcion ,cantidad, lote, vencimiento, laboratorio.
fecha
stock
ingresa
egreso diario
stock mínimo o crítico
saldo mensual
 
"""