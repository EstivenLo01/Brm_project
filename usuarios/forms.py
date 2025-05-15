from django import forms
from . import models
from .models import Empleado
from .models import Campana
from .models import Proveedor
from .models import ActaEquipo
from .models import ActaDiadema
from .models import ProveedorActa



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


class ActaEquipoForm(forms.ModelForm):
    class Meta:
        model = ActaEquipo
        fields = [
            'proveedor',
            'serial_proveedor_cpu',
            'serial_fabrica_cpu',
            'serial_proveedor_monitor',
            'serial_fabrica_monitor',
            'teclado',
            'mouse',
            'monitor',
            'cable_poder',
            'adaptador_corriente',
            'cable_video',
            'cable_red',
            'bolso',
            'cargador',
            'base',
            'guaya',
            'empleado',
            'campana',
            'observaciones',
        ]
        widgets = {
            'observaciones': forms.Textarea(attrs={'rows': 4}),
            'guaya': forms.TextInput(attrs={'placeholder': 'Clave o llave de la guaya'}),
        }
        labels = {
            'serial_proveedor_cpu': 'Serial CPU (Proveedor)',
            'serial_fabrica_cpu': 'Serial CPU (Fábrica)',
            'serial_proveedor_monitor': 'Serial Monitor (Proveedor)',
            'serial_fabrica_monitor': 'Serial Monitor (Fábrica)',
            'cable_video': 'Cable de video (HDMI/VGA/DP)',
            'guaya': 'Guaya (clave o llave)',
        }


class ActaDiademaForm(forms.ModelForm):
    class Meta:
        model = ActaDiadema
        fields = [
            'empleado',
            'marca_diadema',
            'serial_diadema',
            'precio_diadema',
            'campana',
            'observaciones',
        ]
        widgets = {
            'observaciones': forms.Textarea(attrs={'rows': 4}),
            'precio_diadema': forms.NumberInput(attrs={'step': '0.01'}),
        }
        labels = {
            'marca_diadema': 'Marca de la Diadema',
            'serial_diadema': 'Serial de la Diadema',
            'precio_diadema': 'Precio (COP)',
            'observaciones': 'Observaciones (opcional)',
        }




class ProveedorActaForm(forms.ModelForm):
    class Meta:
        model = ProveedorActa
        fields = [
            'proveedor',
            'numero_orden_instalacion',
            'numero_pedido',
            'fecha',
            'empresa',
            'contacto',
            'direccion',
            'ciudad',
            'telefono',
            'equipo',
            'procesador',
            'ram_gb',
            'disco_duro_tb',
            'dvd_writer',
            'entregado_por',
            'recibido_por',
            'observaciones',
        ]
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'observaciones': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'proveedor': 'Proveedor',
            'numero_orden_instalacion': 'N° Orden de Instalación',
            'numero_pedido': 'N° Pedido',
            'fecha': 'Fecha',
            'empresa': 'Empresa',
            'contacto': 'Contacto',
            'direccion': 'Dirección',
            'ciudad': 'Ciudad',
            'telefono': 'Teléfono',
            'equipo': 'Equipo',
            'procesador': 'Procesador',
            'ram_gb': 'Memoria RAM (GB)',
            'disco_duro_tb': 'Disco Duro (TB)',
            'dvd_writer': 'Incluye DVD Writer',
            'entregado_por': 'Entregado por',
            'recibido_por': 'Recibido por',
            'observaciones': 'Observaciones (opcional)',
        }
