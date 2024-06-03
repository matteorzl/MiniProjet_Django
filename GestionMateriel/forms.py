from django import forms
from .models import Enseignant, Materiel, Passation, Salle


class AjoutEnseignantForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ['nom', 'prenom']


class AjoutMaterielForm(forms.ModelForm):
    class Meta:
        model = Materiel
        fields = ['nom', 'accessoires', 'acheteur', 'responsable', 'salle']
        widgets = {
            'acheteur': forms.Select(attrs={'class': 'form-control'}),
            'responsable': forms.Select(attrs={'class': 'form-control'}),
            'salle': forms.Select(attrs={'class': 'form-control'}),
        }


class PassationForm(forms.ModelForm):
    class Meta:
        model = Passation
        fields = ['materiel', 'de', 'a', 'date', 'lieu', 'occasion', 'objectif_utilisation',
                  'accessoires_presents', 'etat_accessoires', 'budget_annee_courante',
                  'budget_projets', 'budget_financements_exceptionnels']


class AjoutSalleForm(forms.ModelForm):
    class Meta:
        model = Salle
        fields = ['numero']

        widgets = {
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
        }