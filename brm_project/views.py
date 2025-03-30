from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms
from usuarios import models
def login(request):
    if request.method == 'POST':
        form = forms.Form_login(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            document_user= form.cleaned_data['document_user']
            if not email or not document_user:
                messages.error(request, 'Los campos no pueden estar vacíos')
                return render(request, "login.html", {'form': form})
            try:
                usuario = models.User.objects.get(document_user=document_user,email=email) 


                #  Comparar con la almacenada en la base de datos
                if document_user.usuario != document_user:
                    messages.error(request, 'Contraseña incorrecta')
                    return render(request, "loginr.html", {'form': form})

                #  Guardar usuario en sesión manualmente
                request.session['user_id'] = usuario.idUser  
                request.session['NombreUsuario'] = usuario.name_user  
                request.session['is_authenticated'] = True  

                #  Redirigir según el rol
                if usuario.id_rol:
                    rol = usuario.id_rol.name_rol
                    if rol == 'administrador':
                        return redirect('administrador:administrador')
                    elif rol == 'digitador_actas':
                        return redirect('digitador_actas:digitador_actas')
                    elif rol == 'supervisor':
                        return redirect('supervisor:supervisor')
                    else:
                        messages.error(request, 'Rol no reconocido')

            except models.User.DoesNotExist:
                messages.error(request, 'No existe un usuario con ese documento')
        
        else:
           messages.error(request, 'Formulario inválido')
           return render(request, "loginr.html", {'form': form})
    else:
        form = forms.Form_login()
    return render(request, 'login.html', {'form':form})
