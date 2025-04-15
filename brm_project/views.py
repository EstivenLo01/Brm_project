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
                usuario = models.User.objects.get(document_user=document_user, email=email)

                # Guardar usuario en sesión manualmente
                request.session['user_id'] = usuario.idUser  
                request.session['NombreUsuario'] = usuario.name_user  
                request.session['is_authenticated'] = True  
                return redirect('usuarios:home')  
            except models.User.DoesNotExist:
                messages.error(request, 'Correo o documento incorrecto')
        else:
           print(form.errors)
           messages.error(request, 'Formulario inválido')
           return render(request, "login.html", {'form': form})
    else:
        form = forms.Form_login()
    return render(request, 'login.html', {'form':form})
