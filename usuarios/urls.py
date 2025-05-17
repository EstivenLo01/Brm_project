from django.urls import path
from . import views
from .views import salir
from django.contrib.auth import views as auth_views



app_name = "usuarios"  # Si defines esto, usa 'usuarios:home' en el redirect

urlpatterns = [
    path("home/", views.home, name="home"),
    path("RegistroUser/", views.RegistroUser, name='RegistroUser'),
    path('Desactivar/<int:idUser>', views.desactivar, name='desactivar'),
    path('registrar_empleado/', views.registrar_empleado, name='registrar_empleado'),
    path('registrar_campana/', views.registrar_campana, name='registrar_campana'),
    path('registrar_acta_equipo/', views.registrar_acta_equipo, name='registrar_acta_equipo'),
    path('registrar_acta_diadema/', views.registrar_acta_diadema, name='registrar_acta_diadema'),
    path('registrar_proveedor/', views.registrar_proveedor, name='registrar_proveedor'),
    path('registrar_acta_proveedor/', views.registrar_acta_proveedor, name='registrar_acta_proveedor'),
    path('inicioSessionXperfil/', views.inicioSessionXperfil, name='inicioSessionXperfil'),
    path('reportes/', views.reportes, name='reportes'),
    path('salir/', salir, name="salir"),
    
    
]


