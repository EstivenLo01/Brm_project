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
    path('editar_empleado/<int:id_empleado>/', views.editar_empleado, name='editar_empleado'),
    path('registrar_campana/', views.registrar_campana, name='registrar_campana'),
    path('editar_campana/<int:id_campana>/', views.editar_campana, name='editar_campana'),
    path('campana/confirmar_habilitar/<int:campana_id>/', views.confirmar_habilitar_campana, name='confirmar_habilitar_campana'),
    path('campana/confirmar_deshabilitar/<int:campana_id>/', views.confirmar_deshabilitar_campana, name='confirmar_deshabilitar_campana'),
    path('registrar_acta_equipo/', views.registrar_acta_equipo, name='registrar_acta_equipo'),
    path('acta_equipo/editar/<int:id_acta>/', views.editar_acta_equipo, name='editar_acta_equipo'),
    path('registrar_acta_diadema/', views.registrar_acta_diadema, name='registrar_acta_diadema'),
    path('editar_acta_diadema/<int:id_acta_diadema>/', views.editar_acta_diadema, name='editar_acta_diadema'),
    path('registrar_proveedor/', views.registrar_proveedor, name='registrar_proveedor'),
    path('editar_proveedor/<int:id_proveedor>/', views.editar_proveedor, name='editar_proveedor'),
    path('registrar_acta_proveedor/', views.registrar_acta_proveedor, name='registrar_acta_proveedor'),
    path('acta_proveedor/editar/<int:id_acta>/', views.editar_acta_proveedor, name='editar_acta_proveedor'),
    path('inicioSessionXperfil/', views.inicioSessionXperfil, name='inicioSessionXperfil'),
    path('automatizar/', views.automatizar_actas, name='automatizar_actas'),
    path('reportes/', views.reportes, name='reportes'),
    path('salir/', salir, name="salir"),
    
    
]


