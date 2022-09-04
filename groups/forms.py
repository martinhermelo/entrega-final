from django import forms

class Formulario_grupos(forms.Form):
    type= forms.CharField(max_length=40)
    team1=forms.CharField(max_length=40)
    team2=forms.CharField(max_length=40)
    team3=forms.CharField(max_length=40)
    team4=forms.CharField(max_length=40)
