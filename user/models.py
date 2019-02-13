from django.db import models

# Create your models here.

class User(models.Model):
    nom = models.CharField(max_length=50, blank=False, null=False)
    prenom = models.CharField(max_length=50, blank=False, null=False)
    mdp = models.CharField(max_length=50, blank=False, null=False, verbose_name="Mot de passe")
    mail = models.EmailField(blank=False, null=False, unique=True, verbose_name="Adresse email")
    tel = models.CharField(max_length=14, null=False, blank=False, unique=True, verbose_name="Telephone")

    def __str__(self):
        return "{} {}".format(self.prenom, self.nom)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

