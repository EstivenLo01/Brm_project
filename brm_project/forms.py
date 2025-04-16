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

class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    nombre_estado = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre_estado
     

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
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
    

class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=150)
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_proveedor
    
class Campaña(models.Model):
    id_campaña = models.AutoField(primary_key=True)
    nombre_campaña = models.CharField(max_length=100)
    estado = models.ForeignKey('Estado', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_campaña
    

class ActaDiadema(models.Model):
    id_acta_diadema = models.AutoField(primary_key=True)
    marca_diadema = models.CharField(max_length=100)
    serial_diadema = models.CharField(max_length=100, unique=True)
    precio_diadema = models.DecimalField(max_digits=10, decimal_places=2)
    cedula_empleado = models.BigIntegerField()
    nombre_empleado = models.CharField(max_length=200)
    campaña = models.CharField(max_length=100)
    observaciones = models.TextField(max_length=100)

    def __str__(self):
        return f"Acta #{self.id_acta_diadema} - {self.nombre_empleado}"
    
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    cedula = models.BigIntegerField(unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    rol = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=128)  # puedes cifrarla si usas auth

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
    
class ActaEquipo(models.Model):
    id_acta_equipo = models.AutoField(primary_key=True)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE)
    serial_proveedor_cpu = models.CharField(max_length=100)
    serial_fabrica_cpu = models.CharField(max_length=100)
    serial_proveedor_monitor = models.CharField(max_length=100, blank=True, null=True)
    serial_fabrica_monitor = models.CharField(max_length=100, blank=True, null=True)
    teclado = models.BooleanField(default=False)
    mouse = models.BooleanField(default=False)
    monitor = models.BooleanField(default=False)
    cable_poder = models.BooleanField(default=False)
    adaptador_corriente = models.BooleanField(default=False)
    cable_video = models.CharField(max_length=50, blank=True, null=True)  # HDMI/VGA/DP
    cable_red = models.BooleanField(default=False)
    bolso = models.BooleanField(default=False)
    cargador = models.BooleanField(default=False)
    base = models.BooleanField(default=False)
    guaya = models.CharField(max_length=50, blank=True, null=True)  # llave o clave
    cedula_empleado = models.BigIntegerField()
    nombre_empleado = models.CharField(max_length=200)
    campaña = models.CharField(max_length=100)
    observaciones = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"ActaEquipo #{self.id_acta_equipo} - {self.nombre_empleado}"
