from django import forms
from usuarios import models

class Form_login(forms.ModelForm):
    email = forms.CharField(
       label="Correo",
       widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    document_user = forms.IntegerField(
        label='Contraseña',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = models.User
        fields = ['email','document_user']


from django.db import models

class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    cedula = models.BigIntegerField(unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono_movil = models.CharField(max_length=15, blank=True, null=True)
    telefono_fijo = models.CharField(max_length=15, blank=True, null=True)
    campaña = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    habilitado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

