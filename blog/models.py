from tabnanny import verbose
from django.db import models

class Notes(models.Model):
    title= models.CharField(max_length=60)
    description= models.CharField(max_length=500)
    author= models.CharField(max_length=100)
    email= models.EmailField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name= "Nota"
        verbose_name_plural= "Notas"