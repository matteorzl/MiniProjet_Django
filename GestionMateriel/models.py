from django.db import models
from django import forms


class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    class Meta:
        app_label = 'GestionMateriel'


class Salle(models.Model):
    numero = models.CharField(max_length=10)

    def __str__(self):
        return self.numero

    @classmethod
    def get_ajout_form(cls):
        class AjoutSalleForm(forms.ModelForm):
            class Meta:
                model = cls
                fields = ['numero']
        return AjoutSalleForm


class Materiel(models.Model):
    nom = models.CharField(max_length=100)
    accessoires = models.TextField(blank=True)
    acheteur = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null=True, related_name='materiels_achetes')
    responsable = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null=True,
                                    related_name='materiels_responsables')
    salle = models.ForeignKey(Salle, on_delete=models.SET_NULL, null=True)
    possesseur = models.ForeignKey(Enseignant, on_delete=models.SET_NULL, null=True, related_name='materiels_possedes')

    def __str__(self):
        return self.nom


class Passation(models.Model):
    materiel = models.ForeignKey(Materiel, on_delete=models.CASCADE)
    de = models.ForeignKey(Enseignant, on_delete=models.CASCADE, related_name='passations_de')
    a = models.ForeignKey(Enseignant, on_delete=models.CASCADE, related_name='passations_a')
    date = models.DateField()
    lieu = models.ForeignKey(Salle, on_delete=models.SET_NULL, null=True)
    occasion = models.CharField(max_length=200, blank=True)
    objectif_utilisation = models.TextField(blank=True)
    accessoires_presents = models.BooleanField(default=True)
    etat_accessoires = models.CharField(max_length=200, blank=True)
    budget_annee_courante = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    budget_projets = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    budget_financements_exceptionnels = models.DecimalField(max_digits=10, decimal_places=2, default=0)
