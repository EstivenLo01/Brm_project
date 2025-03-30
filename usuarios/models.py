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
    def __str__(self):
        return self.name_user
