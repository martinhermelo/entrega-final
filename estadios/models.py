from django.db import models

class Estadios(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to="estadios/",null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name= "Estadio"
        verbose_name_plural= "Estadios"