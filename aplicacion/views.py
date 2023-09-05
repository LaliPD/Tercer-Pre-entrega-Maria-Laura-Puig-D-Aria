from django.shortcuts import render
from .models import Cliente, Empleado, Productos, Proveedores

from .forms import *

from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "aplicacion/home.html")

def cliente(request):
    clientes = Cliente.objects.all()
    contexto = {'clientes': clientes, 'titulo': 'Listado de Clientes'}
    return render(request, 'aplicacion/clientes.html', contexto)

def empleado(request):
    empleados = Empleado.objects.all()
    contexto = {'empleados': empleados}
    return render(request, 'aplicacion/empleados.html', contexto)

def productos(request):
    productos = Productos.objects.all()
    contexto = {'productos': productos}
    return render(request, 'aplicacion/productos.html', contexto)

def proveedores(request):
    proveedores = Proveedores.objects.all()
    contexto = {'proveedores': proveedores}
    return render(request, 'aplicacion/proveedores.html', contexto)


#Buscar Clientes (Search)
def buscarCliente(request):
    return render(request, "aplicacion/buscarCliente.html")

def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        cliente = Cliente.objects.filter(nombre_empresa__icontains=patron)
        contexto = {'clientes': cliente} 
        return render(request, "aplicacion/clientes.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")

#Agregar Clientes
def clienteForm(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            nombre_empresa = form.cleaned_data.get('nombreApellido')
            telefono_contacto = form.cleaned_data.get('telefono_contacto')
            direccion = form.cleaned_data.get('direccion')
            email = form.cleaned_data.get('email')
            cliente = Cliente(nombre_empresa=nombre_empresa, telefono_contacto=telefono_contacto, direccion=direccion, email=email)
            cliente.save()
            return render(request, "aplicacion/base.html")  
    else:
        form = ClienteForm()
    
    return render(request, "aplicacion/clienteForm.html", {"form": form})