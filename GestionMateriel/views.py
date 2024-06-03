from django.shortcuts import render, redirect, get_object_or_404
from .forms import AjoutEnseignantForm, PassationForm, AjoutMaterielForm, AjoutSalleForm
from .models import Enseignant, Materiel, Salle, Passation
from django.urls import reverse
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


#AJOUTER

def ajouter_enseignant(request):
    if request.method == 'POST':
        form = AjoutEnseignantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_enseignants')
    else:
        form = AjoutEnseignantForm()
    return render(request, 'ajouter_enseignant.html', {'form': form})


def ajouter_materiel(request):
    if request.method == 'POST':
        form = AjoutMaterielForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_materiels')
    else:
        form = AjoutMaterielForm()
        salles = Salle.objects.all()
        return render(request, 'ajouter_materiel.html', {'form': form, 'salles': salles})
    return render(request, 'ajouter_materiel.html', {'form': form})


def ajouter_salle(request):
    if request.method == 'POST':
        form = Salle.get_ajout_form()(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_salles')
    else:
        form = Salle.get_ajout_form()()
    return render(request, 'ajouter_salle.html', {'form': form})


#ENREGISTRER

def enregistrer_passation(request):
    initial = {}
    materiel = None

    if 'materiel' in request.GET:
        materiel_id = request.GET['materiel']
        materiel = get_object_or_404(Materiel, pk=materiel_id)
        initial['materiel'] = materiel

    if request.method == 'POST':
        form = PassationForm(request.POST, initial=initial)
        if form.is_valid():
            passation = form.save(commit=False)
            passation.materiel = materiel
            passation.save()
            messages.success(request, 'La passation a été enregistrée avec succès.')
            return redirect(reverse('liste_passations') + f'?materiel={materiel_id}')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Erreur dans le champ '{field}' : {error}")
    else:
        form = PassationForm(initial=initial)

    return render(request, 'enregistrer_passation.html', {'form': form, 'materiel': materiel})


#LISTE

def liste_enseignants(request):
    enseignants = Enseignant.objects.all()
    return render(request, 'liste_enseignants.html', {'enseignants': enseignants})


def liste_materiels(request):
    materiels = Materiel.objects.all()
    return render(request, 'liste_materiels.html', {'materiels': materiels})


def liste_salles(request):
    salles = Salle.objects.all()
    return render(request, 'liste_salles.html', {'salles': salles})


def liste_passations(request):
    passations = Passation.objects.all()
    return render(request, 'liste_passations.html', {'passations': passations})


#MODIFIER

def modifier_materiel(request, id):
    materiel = get_object_or_404(Materiel, pk=id)
    if request.method == 'POST':
        form = AjoutMaterielForm(request.POST, instance=materiel)
        if form.is_valid():
            form.save()
            return redirect('liste_materiels')
    else:
        form = AjoutMaterielForm(instance=materiel)
    return render(request, 'modifier_materiel.html', {'form': form, 'materiel': materiel})


def modifier_enseignant(request, id):
    enseignant = get_object_or_404(Enseignant, pk=id)
    if request.method == 'POST':
        form = AjoutEnseignantForm(request.POST, instance=enseignant)
        if form.is_valid():
            form.save()
            return redirect('liste_enseignants')
    else:
        form = AjoutEnseignantForm(instance=enseignant)
    return render(request, 'modifier_enseignant.html', {'form': form, 'enseignant': enseignant})


def modifier_salle(request, id):
    salle = get_object_or_404(Salle, pk=id)
    if request.method == 'POST':
        form = AjoutSalleForm(request.POST, instance=salle)
        if form.is_valid():
            form.save()
            return redirect('liste_salles')
    else:
        form = AjoutSalleForm(instance=salle)
    return render(request, 'modifier_salle.html', {'form': form, 'salle': salle})


#SUPPRIMER

def supprimer_materiel(request, id):
    materiel = get_object_or_404(Materiel, pk=id)

    if request.method == 'POST':
        materiel.delete()
        return redirect('liste_materiels')

    return render(request, 'supprimer_materiel.html', {'materiel': materiel})


def supprimer_enseignant(request, id):
    enseignant = get_object_or_404(Enseignant, pk=id)
    if request.method == 'POST':
        enseignant.delete()
        return redirect('liste_enseignants')
    return render(request, 'supprimer_enseignant.html', {'enseignant': enseignant})


def supprimer_salle(request, id):
    salle = get_object_or_404(Salle, pk=id)
    if request.method == 'POST':
        salle.delete()
        return redirect('liste_salles')
    return render(request, 'supprimer_salle.html', {'salle': salle})

