from django import forms

class Formulario_estadios(forms.Form):
    name= forms.CharField(max_length=50)
    image=forms.ImageField(required=False)