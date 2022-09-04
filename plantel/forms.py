from django import forms

class Formulario_jugadores(forms.Form):
    full_name = forms.CharField(max_length=40)
    height= forms.FloatField()
    age= forms.IntegerField() 
    club= forms.CharField(max_length=90)
    skillfull_leg= forms.CharField(max_length=20)
    position= forms.CharField(max_length=50)
    image=forms.ImageField(required=False)
