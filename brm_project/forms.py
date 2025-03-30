from django import forms
from usuarios import models

class Form_login(forms.ModelForm):
    email = forms.CharField(
       label="Correo",
       widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    document_user = forms.IntegerField(
        label='Contraseña',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = models.User
        fields = ['email','document_user']
