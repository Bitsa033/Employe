from typing import Any
from django.db import models

# Create your models here.

class Personne(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    age = models.CharField(max_length=100)
    

class Employe(models.Model):
    personne = models.ForeignKey(Personne, on_delete=models.CASCADE)
    date_debut_service = models.DateField(max_length=100)
    duree = models.IntegerField()
    date_fin_service = models.DateField()
    
class Anciennete(models.Model):
    employe= models.ForeignKey(Employe, on_delete=models.CASCADE)
    duree = models.IntegerField()
    reste = models.IntegerField()
