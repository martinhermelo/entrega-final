from django import forms

class Formulario_selecciones(forms.Form):
    name= forms.CharField(max_length=50)
    federation= forms.CharField(max_length=50)