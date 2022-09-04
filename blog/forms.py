from django import forms

class Formulario_notas(forms.Form):
    title= forms.CharField(max_length=60)
    description=forms.CharField(max_length=500)
    author=forms.CharField(max_length=100)
    email=forms.EmailField()