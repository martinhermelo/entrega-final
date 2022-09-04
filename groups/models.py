from django.db import models

class Groups(models.Model):
    type= models.CharField(max_length=40)
    team1=models.CharField(max_length=40)
    team2=models.CharField(max_length=40)
    team3=models.CharField(max_length=40)
    team4=models.CharField(max_length=40)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name= "Group"
        verbose_name_plural= "Groups"

