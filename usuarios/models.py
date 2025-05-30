from django.db import models




# Create your models here.

#Tabla roles
class Rol(models.Model):
    idRol = models.AutoField(primary_key=True)
    name_rol = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name_rol

#Tabla tipo documento
class TypeDocument(models.Model):
    idType_document = models.AutoField(primary_key=True)
    name_document = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name_document
#Tabla Estado
class Estado(models.Model):
    ID_Estado = models.AutoField(primary_key=True)
    Nombre_Estado = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.Nombre_Estado

class User(models.Model):
    idUser = models.AutoField(primary_key=True)
    name_user = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    idType_document = models.ForeignKey(TypeDocument, on_delete=models.CASCADE)
    document_user = models.BigIntegerField(unique=True)
    idRol =models.ForeignKey(Rol, on_delete=models.CASCADE)
    email = models.CharField(max_length=100)
    contact = models.BigIntegerField()
    contact_two = models.BigIntegerField()
    date_creation =models.DateTimeField(auto_now=True)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.name_user
        

    
class Campana(models.Model):
    id_campana = models.AutoField(primary_key=True)
    nombre_campana = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_campana


class Empleado(models.Model):
    id_empleado = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=20, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono_movil = models.CharField(max_length=15)
    telefono_fijo = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=255)
    campana = models.ForeignKey(Campana, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - {self.cedula}"
    

class Proveedor(models.Model):
    id_proveedor = models.CharField(max_length=20, primary_key=True)
    nombre_proveedor = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_proveedor
    

class marca_diadema(models.Model):
    id_marca_diadema = models.AutoField(primary_key=True)
    nombre_marca_diadema = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nombre_marca_diadema
    

class ActaDiadema(models.Model):
    id_acta_diadema = models.AutoField(primary_key=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    marca_diadema = models.ForeignKey(marca_diadema, on_delete=models.CASCADE)
    serial_diadema = models.CharField(max_length=50, unique=True)
    precio_diadema = models.DecimalField(max_digits=10, decimal_places=2)
    campana = models.ForeignKey(Campana, on_delete=models.CASCADE)
    observaciones = models.TextField(blank=True, null=True)
    archivo = models.FileField(upload_to='actas_diadema/', blank=True, null=True)

    def __str__(self):
        return f"ActaDiadema #{self.id_acta_diadema} - {self.empleado.nombres} ({self.empleado.cedula})"
    
class ActaEquipo(models.Model):
    id_acta_equipo = models.AutoField(primary_key=True)
    
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    serial_proveedor_cpu = models.CharField(max_length=100)
    serial_fabrica_cpu = models.CharField(max_length=100)
    serial_proveedor_monitor = models.CharField(max_length=100)
    serial_fabrica_monitor = models.CharField(max_length=100)

    teclado = models.BooleanField(default=False)
    mouse = models.BooleanField(default=False)
    monitor = models.BooleanField(default=False)
    cable_poder = models.BooleanField(default=False)
    adaptador_corriente = models.BooleanField(default=False)
    cable_video = models.BooleanField(default=False)  # HDMI/VGA/DP
    cable_red = models.BooleanField(default=False)
    bolso = models.BooleanField(default=False)
    cargador = models.BooleanField(default=False)
    base = models.BooleanField(default=False)
    guaya = models.CharField(max_length=20, blank=True, null=True)  # clave o llave

    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    campana = models.ForeignKey(Campana, on_delete=models.CASCADE)

    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"ActaEquipo #{self.id_acta_equipo} - {self.empleado.nombres} ({self.empleado.cedula})"
    

class ProveedorActa(models.Model):
    id_ProveedorActa = models.AutoField(primary_key=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    numero_orden_instalacion = models.CharField(max_length=50)
    numero_pedido = models.CharField(max_length=50)
    fecha = models.DateField()
    
    empresa = models.CharField(max_length=100, default='BRM S.A.S')
    contacto = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    equipo = models.CharField(max_length=100)
    procesador = models.CharField(max_length=100)
    ram_gb = models.IntegerField()
    disco_duro_tb = models.FloatField()
    dvd_writer = models.BooleanField(default=False)

    entregado_por = models.CharField(max_length=100)
    recibido_por = models.CharField(max_length=100, blank=True, null=True)

    observaciones = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"Acta #{self.numero_orden_instalacion} - {self.contacto}"
    




