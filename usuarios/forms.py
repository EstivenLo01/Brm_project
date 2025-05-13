from django import forms
from . import models
from .models import Empleado
from .models import Campana
from .models import Proveedor



class RegistroUser(forms.ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'
        labels = {
            'name_user': 'Nombre',
            'last_name': 'Apellido',
            'idType_document': 'Tipo de documento',
            'document_user': 'Número de documento',
            'idRol': 'Rol',
            'email': 'Correo electrónico',
            'contact': 'Contacto principal',
            'contact_two': 'Contacto secundario',
            'date_creation': 'Fecha de creación',
        }
        widgets = {
            'name_user': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el apellido'
            }),
            'idType_document': forms.Select(attrs={
                'class': 'form-select'
            }),
            'document_user': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el número de documento'
            }),
            'idRol': forms.Select(attrs={
                'class': 'form-select'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ejemplo@correo.com'
            }),
            'contact': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de celular'
            }),
            'contact_two': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Otro número (opcional)'
            }),
            'date_creation': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
        }

class desactivar(forms.ModelForm):
   class Meta:
        model = models.User
        fields = ['id_estado']



class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'direccion': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class CampanaForm(forms.ModelForm):
    class Meta:
        model = Campana
        fields = ['nombre_campana', 'estado']


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre_proveedor', 'estado']