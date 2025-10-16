from django.db import models



class  DepositoAmpollas(models.Model):

  idAmpolla = models.AutoField(primary_key=True)
  nombreMedicamento = models.TextField(max_length=255)
  lote= models.CharField(max_length=255)
  vencimiento = models.DateField()
  laboratorio = models.CharField(max_length=255)
  fecha= models.DateField()
  stockCritico = models.IntegerField()
  cantidadStock = models.IntegerField()
  cantDispensada= models.IntegerField()
  cantIngresada=models.IntegerField()
  SaldoMensual=models.IntegerField()
# Create your models here.
"""idAmpollas, descripcion ,cantidad, lote, vencimiento, laboratorio.
fecha
stock
ingresa
egreso diario
stock mínimo o crítico
saldo mensual
 
"""