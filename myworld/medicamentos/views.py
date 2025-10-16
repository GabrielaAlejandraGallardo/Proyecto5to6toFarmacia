"""from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world!")"""

"""from django.http import HttpResponse
from django.template import loader
from .models import Members


def index(request):
  mymembers = Members.objects.all().values()
  output = ""
  for x in mymembers:
    output += x["firstname"]
  return HttpResponse(output)
"""
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse
from .models import DepositoAmpollas
from datetime import datetime




def inicio(request):
    return render(request,'inicio.html')
  
def index(request):
  mymembers = DepositoAmpollas.objects.all().values()
  template = loader.get_template('index.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))


# ...existing code...

def addrecord(request):
    if request.method == "POST":
        nombre = request.POST['nombreMedicamento']
        lote= request.POST['lote']
        vencimiento_str = request.POST['vencimiento']
        laboratorio= request.POST['laboratorio']
        fecha_str= request.POST['fecha']
        stockCritico= request.POST['stockCritico']
        cantidad = request.POST['cantidadStock']
        dispensada = request.POST['cantDispensada']
        ingresada = request.POST['cantIngresada']
        saldoMensual= request.POST['SaldoMensual']

        # Convert date strings to date objects
        vencimiento = datetime.strptime(vencimiento_str, '%Y-%m-%d').date()
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()

        member=DepositoAmpollas(
            nombreMedicamento=nombre,
            lote=lote,
            vencimiento=vencimiento,
            laboratorio=laboratorio,
            fecha=fecha,
            stockCritico=stockCritico,
            cantidadStock=cantidad,
            cantDispensada=dispensada,
            cantIngresada=ingresada,
            SaldoMensual=saldoMensual
        )
        member.save()
        return redirect('/medicamentos/index')












# ...existing code...
def delete(request, idAmpolla):
  member = DepositoAmpollas.objects.get(idAmpolla=idAmpolla)
  member.delete()
  return HttpResponseRedirect(reverse('index'))


def update(request, idAmpolla):
  mymember = DepositoAmpollas.objects.get(id=idAmpolla)
  template = loader.get_template('update.html')
  context = {  'mymember': mymember,  }
  return HttpResponse(template.render(context, request))

# ...existing code...
def updaterecord(request, id):
    if request.method == "POST":
        nombre = request.POST['nombreMedicamento']
        lote = request.POST['lote']
        vencimiento_str = request.POST['vencimiento']
        laboratorio = request.POST['laboratorio']
        fecha_str = request.POST['fecha']
        stockCritico = request.POST['stockCritico']
        cantidad = request.POST['cantidadStock']
        dispensada = request.POST['cantDispensada']
        ingresada = request.POST['cantIngresada']
        saldoMensual = request.POST['SaldoMensual']

        # Convert date strings to date objects
        vencimiento = datetime.strptime(vencimiento_str, '%Y-%m-%d').date()
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()

        member = DepositoAmpollas.objects.get(id=id)
        member.nombreMedicamento = nombre
        member.lote = lote
        member.vencimiento = vencimiento
        member.laboratorio = laboratorio
        member.fecha = fecha
        member.stockCritico = stockCritico
        member.cantDispensada = dispensada
        member.cantIngresada = ingresada
        member.cantidadStock = int(cantidad) - int(dispensada) + int(ingresada)
        member.SaldoMensual = saldoMensual
        member.save()
        return redirect('/medicamentos/index')








































































































