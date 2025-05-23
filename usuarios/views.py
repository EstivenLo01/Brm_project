from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from . import models, forms
from django.urls import reverse
from django.db.models import Q
from .forms import EmpleadoForm
from .forms import CampanaForm
from .models import Campana
from .models import Empleado
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import ProveedorForm
from .models import Proveedor
from usuarios.models import Estado





def home(request):
    usuario = request.session.get('NombreUsuario','NO')
    if not request.session.get('is_authenticated'):
        return redirect('/login/')
    usuario = models.User.objects.get(name_user=usuario)
    if usuario.idRol:
        rol = usuario.idRol.name_rol
        if rol == 'administrador':
           print('administrador')
           #backend para el superadmin
           x = reverse('usuarios:RegistroUser')    
           x2 = reverse('usuarios:registrar_acta_equipo')
           x3 = reverse('usuarios:registrar_acta_diadema')
           x4 = reverse('usuarios:registrar_proveedor')
           x5 = reverse('usuarios:registrar_acta_proveedor')
           y = reverse('usuarios:registrar_empleado')
           x7 = reverse('usuarios:registrar_campana')
           x8 = reverse('usuarios:inicioSessionXperfil')
           x9 = reverse('usuarios:reportes')
           context = {
                'icono_uno': 'fa-solid fa-user-plus',
                'nombre_uno': 'Registrar Usuario',
                'icono_dos': 'fa-solid fa-laptop',
                'nombre_dos': 'Registrar Acta Equipo',
                'icono_tres': 'fa-solid fa-headset',
                'nombre_tres': 'Registrar Acta Diadema',
                'icono_cuatro': 'fa-solid fa-handshake',
                'nombre_cuatro': 'Registrar Proveedor',
                'icono_cinco': 'fa-solid fa-file-signature',
                'nombre_cinco': 'Registrar Acta Proveedor',
                'icono_seis': 'fa-solid fa-id-badge',
                'nombre_seis': 'Registrar Empleado',
                'icono_siete': 'fa-solid fa-bullhorn',
                'nombre_siete': 'Registrar Campaña',
                'icono_ocho': 'fa-solid fa-right-to-bracket',
                'nombre_ocho': 'Inicio De Sesion X Perfil',
                'icono_nueve': 'fa-solid fa-chart-line',
                'nombre_nueve': 'Reportes',
                'opcion_uno':  x,
                'opcion_dos':  x2,
                'opcion_tres': x3,
                'opcion_cuatro': x4,
                'opcion_cinco': x5,
                'opcion_seis': y,
                'opcion_siete': x7,
                'opcion_ocho': x8,
                'opcion_nueve': x9,
                'usuario': usuario,}
           return render(request, 'usuarios/home.html',context)
        
        
        

        elif rol == 'digitador_actas':
             #backend para quien digita las actas
            x1 = reverse('usuarios:registrar_acta_equipo')
            x2 = reverse('usuarios:registrar_acta_diadema')
            x3 = reverse('usuarios:registrar_acta_proveedor')
            x4 = reverse('usuarios:automatizar_actas')
            context = {
                'icono_uno': 'fa-solid fa-folder-plus',
                'nombre_uno': 'Registrar Acta Proveedor',
                'icono_dos': 'fa-solid fa-folder-plus',
                'nombre_dos': 'Registrar Acta Equipo',
                'icono_tres': 'fa-solid fa-headset',
                'nombre_tres': 'Registrar Acta Diadema', 
                'icono_cuatro': 'fa-solid fa-wand-sparkles',
                'nombre_cuatro': 'Automatizar Actas',
                'rol': rol,
                'opcion_uno': x3,
                'opcion_dos':  x1,
                'opcion_tres': x2,
                'opcion_cuatro': x4,
                'usuario': usuario,     }

            return render(request, 'usuarios/home.html', context )
        elif rol == 'supervisor':
            print('supervisor')
             #backend para administrador
            x2 = reverse('usuarios:registrar_acta_equipo')
            x3 = reverse('usuarios:registrar_acta_diadema')
            x4 = reverse('usuarios:registrar_proveedor')
            x5 = reverse('usuarios:registrar_acta_proveedor')
            y = reverse('usuarios:registrar_empleado')
            x7 = reverse('usuarios:registrar_campana')
            x8 = reverse('usuarios:inicioSessionXperfil')
            x9 = reverse('usuarios:reportes')
            context = {
               'icono_uno': 'fa-solid fa-laptop',
                'nombre_uno': 'Registrar Acta Equipo',
                'icono_tres': 'fa-solid fa-headset',
                'nombre_tres': 'Registrar Acta Diadema',
                'icono_cuatro': 'fa-solid fa-handshake',
                'nombre_cuatro': 'Registrar Proveedor',
                'icono_cinco': 'fa-solid fa-file-signature',
                'nombre_cinco': 'Registrar Acta Proveedor',
                'icono_seis': 'fa-solid fa-id-badge',
                'nombre_seis': 'Registrar Empleado',
                'icono_siete': 'fa-solid fa-bullhorn',
                'nombre_siete': 'Registrar Campaña',
                'icono_ocho': 'fa-solid fa-right-to-bracket',
                'nombre_ocho': 'Inicio De Sesion X Perfil',
                'icono_nueve': 'fa-solid fa-chart-line',
                'nombre_nueve': 'Reportes',
                'rol': rol,
                'opcion_uno':  x2,
                'opcion_tres': x3,
                'opcion_cuatro': x4,
                'opcion_cinco': x5,
                'opcion_seis': y,
                'opcion_siete': x7,
                'opcion_ocho': x8,
                'opcion_nueve': x9,
                'usuario': usuario,}
            return render(request, 'usuarios/home.html', context )

        else:
            messages.error(request, 'Rol no reconocido')
            return render(request, 'usuarios/home.html',{'usuario': usuario})
        
        

def salir(request):
    logout(request)
    messages.success(request, "Tu sesion ha finalizado correctamente")
    return redirect("login")
        

# Regsitro de usuarios
def RegistroUser(request):
    usuario = request.session.get('NombreUsuario','NO')
    if not request.session.get('is_authenticated'):
        return redirect('/login/')
    usuario = models.User.objects.get(name_user=usuario)
    if request.method == 'POST':
        form = forms.RegistroUser(request.POST)
        if form.is_valid:
            form.save()
    else:
        form = forms.RegistroUser()
    query = request.GET.get('buscar', '')
    if query:
        usuarios = models.User.objects.filter(
            Q(name_user__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query) |
            Q(contact__icontains=query) |
            Q(document_user__icontains=query)
        )
    else:
        usuarios = models.User.objects.all()
    # usuarios = models.User.objects.all()
    context={
        'form': form,
        'usuarios': usuarios,
        'usuario': usuario,
        'query': query,
    }
    return render(request, 'usuarios/registroUser.html',context)

def desactivar(request, idUser):
    usuario = request.session.get('NombreUsuario','NO')
    if not request.session.get('is_authenticated'):
        return redirect('/login/')
    usuario = models.User.objects.get(name_user=usuario)
    desactivar = models.User.objects.get(idUser=idUser)
    context={
        'usuario': usuario,
    }
    if request.method == 'POST':
        form = forms.desactivar(request.POST, instance=desactivar)
        if form.is_valid():
            form.save()
            return render(request, 'usuarios/desactivar.html', context)
    else:
        form = forms.desactivar(instance=desactivar)
    return render(request, 'usuarios/desactivar.html', context)



def registrar_campana(request):
    if request.method == 'POST':
        form = CampanaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios:registrar_campana')
    else:
        form = CampanaForm()
    
    campanas = Campana.objects.all()
    return render(request, 'usuarios/registrar_campana.html', {
        'form': form,
        'campanas': campanas
    })



def registrar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # O a una página de éxito
    else:
        form = EmpleadoForm()
    return render(request, 'usuarios/registrar_empleado.html', {'form': form})


def registrar_acta_equipo(request):
    return render(request, 'usuarios/registrar_acta_equipo.html')

def registrar_acta_diadema(request):
    return render(request, 'usuarios/registrar_acta_diadema.html')


def registrar_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios:registrar_proveedor')  # Redirige después de guardar
    else:
        form = ProveedorForm()

    proveedores = Proveedor.objects.all()  # Para mostrar la tabla
    return render(request, 'usuarios/registrar_proveedor.html', {'form': form, 'proveedores': proveedores})


def registrar_acta_proveedor(request):
    return render(request, 'usuarios/registrar_acta_proveedor.html')

def inicioSessionXperfil(request):
    return render(request, 'usuarios/inicioSessionXperfil.html')


def reportes(request):
    return render(request, 'usuarios/reportes.html')


def automatizar_actas(request):
    return render(request, 'usuarios/automatizar_actas.html')