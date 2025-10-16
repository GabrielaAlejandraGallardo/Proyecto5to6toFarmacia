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
        cantidad = request.POST['cantidadStock']
        dispensada = request.POST['cantDispensada']
        ingresada = request.POST['cantIngresada']
      
        member=DepositoAmpollas(
            nombreMedicamento=nombre,
            cantidadStock=cantidad,
            cantDispensada=dispensada,
            cantIngresada=ingresada,
        )
        member.save()
        return redirect('/medicamentos/index')


# ...existing code...
def delete(request, id):
  member = DepositoAmpollas.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))


def update(request, id):
  mymember = DepositoAmpollas.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {  'mymember': mymember,  }
  return HttpResponse(template.render(context, request))

# ...existing code...
def updaterecord(request, id):
    if request.method == "POST":
        nombre = request.POST['nombreMedicamento']
        cantidad = request.POST['cantidadStock']
        dispensada = request.POST['cantDispensada']
        ingresada = request.POST['cantIngresada']
        member = DepositoAmpollas.objects.get(id=id)
        member.nombreMedicamento = nombre
        member.cantDispensada = dispensada
        member.cantIngresada = ingresada
        member.cantidadStock = int(cantidad) - int(dispensada)+int(ingresada)
        member.save() 
        return redirect('/medicamentos/index')








































































































