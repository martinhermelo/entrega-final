from django.db import models

class Plantel(models.Model):
    full_name = models.CharField(max_length=70,)
    height= models.FloatField()
    age= models.IntegerField() 
    club= models.CharField(max_length=90)
    skillfull_leg= models.CharField(max_length=20)
    position= models.CharField(max_length=50)
    image= models.ImageField(upload_to="plantel/", null=True,blank=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name= "Jugador"
        verbose_name_plural= "Jugadores"