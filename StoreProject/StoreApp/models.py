from django.db import models
# Create your models here.
class Produit(models.Model):
    nom=models.CharField(max_length=255,null=False)
    description=models.TextField(blank=True,null=False)
    prix=models.FloatField(null=False)
    quantite=models.IntegerField(null=False)
    image=models.ImageField(upload_to='images/',null=False)
    def __str__(self):
        return self.nom

class User(models.Model):
    nom=models.CharField(max_length=255, null=False)
    prenom = models.CharField(max_length=255, null=False)
    ddn=models.DateField()
    mail = models.EmailField(max_length=255, null=False,unique=True)
    password=models.CharField(max_length=255,null=False)
    phone=models.CharField(max_length=255, null=False)
    USERNAME_FIELD = 'email'





