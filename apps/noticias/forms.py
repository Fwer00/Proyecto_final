from django import forms
from .models import Comentario, Noticia, Categoria

class ComentarioForm(forms.ModelForm):
    class Meta:
        model=Comentario
        fields=['texto']
        widgets = {
            'texto' : forms.Textarea(attrs={'class':'form-control', 'rows': '3', 'placeholder':"Escribe un comentario..."}),
        }

class NoticiaForm(forms.ModelForm):
    class Meta:
        model=Noticia
        fields=['titulo', 'resumen', 'cuerpo', 'imagen', 'categoria_noticia']
        widgets = {
            'titulo' : forms.Textarea(attrs={'class':'form-control', 'rows': '1', 'placeholder':"Escribe un titulo..."}),
            'resumen' : forms.Textarea(attrs={'class':'form-control', 'rows': '3', 'placeholder':"Escribe un extracto..."}),
            'cuerpo' : forms.Textarea(attrs={'class':'form-control', 'rows': '10', 'placeholder':"Escribe el contenido..."}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model=Categoria
        fields=['nombre']
        widgets = {
            'nombre' : forms.Textarea(attrs={'class':'form-control', 'rows': '1', 'placeholder':"Escribe un categoria..."}),
        }
    
