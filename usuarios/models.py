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
    cedula = models.CharField(max_length=20)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono_movil = models.CharField(max_length=15)
    telefono_fijo = models.CharField(max_length=15, blank=True, null=True)
    campana = models.ForeignKey(Campana, on_delete=models.CASCADE)
    direccion = models.TextField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
    

class Proveedor(models.Model):
    id_proveedor = models.CharField(max_length=20, primary_key=True)
    nombre_proveedor = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_proveedor