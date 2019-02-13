from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('ajouter', views.ajouter_user, name="user.add"),
    path('modifier/<str:mail>', views.modifier_user, name="user.update"),
    path('supprimer/<str:mail>', views.supprimer_user, name="user.delete"),
]