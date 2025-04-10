

from . import views


from django.contrib import admin
from django.urls import path
from RealEstateAgency import views




from django.urls import path
# RealEstateAgency/urls.py
from .views import AppartementListView, MaisonListView, TerrainListView

from .views import PropertyMapView



urlpatterns = [
    # Routes pour Maison
    path('maisons/search/', views.search_maisons, name='search-maisons'),  # Recherche des maisons avec filtrage
    path('maisons/create/', views.create_maison, name='create-maison'),
    path('maisons/<int:pk>/', views.get_maison, name='get-maison'),
    path('maisons/update/<int:pk>/', views.update_maison, name='update-maison'),
    path('maisons/delete/<int:pk>/', views.delete_maison, name='delete-maison'),

    # Routes pour Appartement
    path('appartements/search/', views.search_appartements, name='search-appartements'),  # Recherche des appartements avec filtrage
    path('appartements/create/', views.create_appartement, name='create-appartement'),
    path('appartements/<int:pk>/', views.get_appartement, name='get-appartement'),
    path('appartements/update/<int:pk>/', views.update_appartement, name='update-appartement'),
    path('appartements/delete/<int:pk>/', views.delete_appartement, name='delete-appartement'),

    # Routes pour Terrain
    path('terrains/search/', views.search_terrains, name='search-terrains'),  # Recherche des terrains avec filtrage
    path('terrains/create/', views.create_terrain, name='create-terrain'),
    path('terrains/<int:pk>/', views.get_terrain, name='get-terrain'),
    path('terrains/update/<int:pk>/', views.update_terrain, name='update-terrain'),
    path('terrains/delete/<int:pk>/', views.delete_terrain, name='delete-terrain'),
    
     # Routes pour Client
    path('clients/search/', views.search_clients, name='search-clients'),
    path('clients/create/', views.create_client, name='create-client'),
    path('clients/<int:id>/', views.get_client, name='get-client'),
    path('clients/update/<int:id>/', views.update_client, name='update-client'),
    path('clients/delete/<int:id>/', views.delete_client, name='delete-client'),

    # Routes pour Transaction
     path('transactions/search/', views.search_transactions, name='search-transactions'),
    path('transactions/create/', views.create_transaction, name='create-transaction'),
    path('transactions/<int:id>/', views.get_transaction, name='get-transaction'),
    path('transactions/update/<int:id>/', views.update_transaction, name='update-transaction'),
    path('transactions/delete/<int:id>/', views.delete_transaction, name='delete-transaction'),

    
    
    
    # Route pour accéder à la vue avec type et ID de propriété
    path('api/properties/<str:property_type>/<int:property_id>/map/', PropertyMapView.as_view(), name='property-map'),

  
    
    ]
