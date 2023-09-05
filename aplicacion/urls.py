from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name = "home" ),
    path('clientes/', cliente, name = "clientes" ),
    path('empleados/', empleado, name = "empleados" ),
    path('productos/', productos, name = "productos" ),
    path('proveedores/', proveedores, name = "proveedores" ),

     path('buscar_cliente/', buscarCliente, name="buscar_cliente"),
     path('buscar2/', buscar2, name="buscar2"),

     path('cliente_form/', clienteForm, name="cliente_form"),
    
    
]