from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Rol)
admin.site.register(models.TypeDocument)
admin.site.register(models.User)
admin.site.register(models.Campana)
admin.site.register(models.Proveedor)