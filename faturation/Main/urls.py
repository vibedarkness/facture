from django.urls import path
from Main import views

urlpatterns = [
    path('', views.IndexView.as_view(),name='acceuil'),
    path('ajouter_client', views.ClientView.as_view(),name='add_client'),
    path('ajouter_facture', views.FactureView.as_view(),name='add_facture')
]