from django import forms
from usuarios import models

class Form_login(forms.Form):
    email = forms.EmailField(
        label="Correo",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    document_user = forms.IntegerField(
        label='Documento',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )


