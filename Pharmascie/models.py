from django.db import models

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Pharmacie(models.Model):
    nom_Pharmacie = models.CharField(db_column='Nom Pharmacie', max_length=255)  # Field name made lowercase.
    adresse = models.CharField(db_column='Adresse', max_length=255)  # Field name made lowercase.
    Locality= models.CharField(db_column='Locality', max_length=255)
    
    City_District_Town= models.CharField(db_column='City_District_Town', max_length=255)
    PinCode= models.CharField(db_column='PinCode', max_length=255)
    state= models.CharField(db_column='state', max_length=255)
    
    tel = models.CharField(db_column='Tel', max_length=255)  # Field name made lowercase.
    position_lat = models.DecimalField(max_digits=6, decimal_places=6)
    position_lng = models.DecimalField(max_digits=6, decimal_places=6)
    
    sidegarde = models.BooleanField(default=False,db_column='sidegarde',max_length=26)  # Field name made lowercase.
    idutil = models.ForeignKey('Acount.Utilisateur2', models.DO_NOTHING, db_column='idutil')

    class Meta:
        db_table = 'Pharmacie'
