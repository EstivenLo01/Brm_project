from django import forms
from usuarios import models


class Form_login(forms.Form):
    email = forms.EmailField(
        label="Correo",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    document_user = forms.IntegerField(
        label='Contraseña',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )


# class EstadoForm(forms.ModelForm):
#     class Meta:
#         model = Estado
#         fields = ['Nombre_Estado']  # No se incluye ID_Estado porque se genera automáticamente
#         widgets = {
#             'Nombre_Estado': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Ingrese el nombre del estado'
#             }),
#         }
#         labels = {
#             'Nombre_Estado': 'Nombre del Estado'
#         }
