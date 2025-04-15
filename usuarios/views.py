from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from . import models

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
           context = {'usuario': usuario, 'rol': rol}
           return render(request, 'usuarios/home.html',{'usuario': usuario})
        elif rol == 'digitador_actas':
            print('digitador_actas')
             #backend para quien digita las actas
            context = {'usuario': usuario, 'rol': rol}
            return render(request, 'usuarios/home.html',context)
        elif rol == 'supervisor':
            print('supervisor')
             #backend para administrador
        else:
            messages.error(request, 'Rol no reconocido')
            return render(request, 'usuarios/home.html',{'usuario': usuario})
