from django.db import models

# Create your models here.
from django.db import models


class Utilisateur2(models.Model):
    Real_name = models.CharField(max_length=255)
    Email=models.EmailField(unique=True)
    Password = models.CharField(max_length=255)
    #Confirm_Password = models.CharField(max_length=255)
    Type_counte = models.BooleanField(default=False,max_length=26)  # Field name made lowercase.
    #Country=models.CharField(max_length=255)
    #Ville = models.ForeignKey('Ville', models.DO_NOTHING, db_column='Ville')
    class Meta:
        managed = True
        db_table = 'Utilisateur'
    def __str__(self) :
        return self.Real_name
