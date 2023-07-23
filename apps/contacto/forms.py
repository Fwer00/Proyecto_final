from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Contacto
        fields = ["nombre", "correo", "mensaje"]

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coloca tu nombre completo'}),
            'correo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu correo electronico'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Detalla tu mensaque aqui...'}),
        }