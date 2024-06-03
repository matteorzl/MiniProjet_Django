from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('liste_enseignants/', views.liste_enseignants, name='liste_enseignants'),
    path('ajouter_enseignant/', views.ajouter_enseignant, name='ajouter_enseignant'),
    path('modifier_enseignant/<int:id>/', views.modifier_enseignant, name='modifier_enseignant'),
    path('supprimer_enseignant/<int:id>/', views.supprimer_enseignant, name='supprimer_enseignant'),
    path('liste_materiels/', views.liste_materiels, name='liste_materiels'),
    path('ajouter_materiel/', views.ajouter_materiel, name='ajouter_materiel'),
    path('modifier_materiel/<int:id>/', views.modifier_materiel, name='modifier_materiel'),
    path('supprimer_materiel/<int:id>/', views.supprimer_materiel, name='supprimer_materiel'),
    path('liste_salles/', views.liste_salles, name='liste_salles'),
    path('ajouter_salle/', views.ajouter_salle, name='ajouter_salle'),
    path('modifier_salle/<int:id>/', views.modifier_salle, name='modifier_salle'),
    path('supprimer_salle/<int:id>/', views.supprimer_salle, name='supprimer_salle'),
    path('liste_passations/', views.liste_passations, name='liste_passations'),
    path('enregistrer_passation/', views.enregistrer_passation, name='enregistrer_passation'),
]