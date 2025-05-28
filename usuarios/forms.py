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
    cedula = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Cédula'
    )
    nombres = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Nombres'
    )
    apellidos = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Apellidos'
    )
    correo = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        label='Correo Electrónico'
    )
    telefono_movil = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Teléfono Móvil'
    )
    telefono_fijo = forms.CharField(
        max_length=15,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Teléfono Fijo (opcional)'
    )
    direccion = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Dirección'
    )
    campana = forms.ModelChoiceField(
        queryset=Campana.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Campaña'
    )
    estado = forms.ModelChoiceField(
        queryset=models.Estado.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Estado'
    )
    class Meta:
        model = Empleado
        fields = '__all__'
        
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
    empleado = forms.ModelChoiceField(
        queryset=Empleado.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Empleado'
    )
    marca_diadema = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Marca de la Diadema'
    )
    serial_diadema = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Serial de la Diadema'
    )
    precio_diadema = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        label='Precio (COP)'
    )
    campana = forms.ModelChoiceField(
        queryset=Campana.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Campaña'
    )
    observaciones = forms.CharField(
        max_length=500,
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        label='Observaciones (opcional)'
    )
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




class ProveedorActaForm(forms.ModelForm):
    proveedor = forms.ModelChoiceField(
        queryset=Proveedor.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Proveedor'
    )
    numero_orden_instalacion= forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Número de Orden de Instalación'
    )
    numero_pedido = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Número de Pedido'
    )
    fecha = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        label='Fecha'
    )
    empresa = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Empresa'
    )
    contacto = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Contacto'
    )
    direccion = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Dirección'
    )
    ciudad = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Ciudad'
    )
    telefono = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Teléfono'
    )
    equipo = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Equipo'
    )
    procesador = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Procesador'
    )
    ram_gb = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label='RAM (GB)'
    )
    disco_duro_tb = forms.FloatField(
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
        label='Disco Duro (TB)'
    )
    dvd_writer = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        label='DVD Writer'
    )
    entregado_por = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Entregado por'
    )
    recibido_por = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Recibido por'
    )
    observaciones = forms.CharField(
        max_length=500,
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        label='Observaciones'
    )
    class Meta:
        model = ProveedorActa
        fields = '__all__'
