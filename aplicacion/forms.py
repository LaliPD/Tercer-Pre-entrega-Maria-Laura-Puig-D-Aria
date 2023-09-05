from django import forms


class ClienteForm(forms.Form):
    nombre_empresa = forms.CharField(max_length=100)
    telefono_contacto = forms.CharField(max_length=20)
    direccion = forms.CharField (max_length=100)
    email = forms.EmailField()