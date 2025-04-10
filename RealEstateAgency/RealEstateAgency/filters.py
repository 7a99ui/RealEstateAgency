import django_filters
from .models import Maison, Appartement, Terrain , Client



import django_filters
from .models import Appartement, Maison, Terrain


# Fonction de nettoyage des espaces
def clean_spaces(value):
    if value and isinstance(value, str):  # Vérifie que la valeur est une chaîne et non vide
        return ' '.join(value.split()).strip()  # Supprime les espaces excédentaires
    return value



class AppartementFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title')
    city = django_filters.CharFilter(lookup_expr='icontains', label='City')
    property = django_filters.CharFilter(lookup_expr='icontains', label='Property')
    area_min = django_filters.NumberFilter(field_name='area', lookup_expr='gte', label='Min Area')
    area_max = django_filters.NumberFilter(field_name='area', lookup_expr='lte', label='Max Area')
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Min Price')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Max Price')
    is_sold = django_filters.BooleanFilter(field_name='is_sold', label='Is Sold')
    rooms_min = django_filters.NumberFilter(field_name='rooms', lookup_expr='gte', label='Min Rooms')
    rooms_max = django_filters.NumberFilter(field_name='rooms', lookup_expr='lte', label='Max Rooms')

    class Meta:
        model = Appartement
        fields = ['title', 'city', 'property', 'area', 'price', 'is_sold', 'rooms']
        
    # Méthode de filtre pour nettoyer les espaces dans le titre
    def filter_title(self, queryset, name, value):
        value = clean_spaces(value)  # Appliquer la normalisation des espaces
        return queryset.filter(**{name + '__icontains': value})

class MaisonFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title')
    city = django_filters.CharFilter(lookup_expr='icontains', label='City')
    property = django_filters.ChoiceFilter(choices=[
        ('Maison', 'Maison'),
        ('Terrain', 'Terrain'),
        ('Appartement', 'Appartement')
    ], label='Property')
    area_min = django_filters.NumberFilter(field_name='area', lookup_expr='gte', label='Min Area')
    area_max = django_filters.NumberFilter(field_name='area', lookup_expr='lte', label='Max Area')
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Min Price')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Max Price')
    is_sold = django_filters.BooleanFilter(field_name='is_sold', label='Is Sold')
    rooms_min = django_filters.NumberFilter(field_name='rooms', lookup_expr='gte', label='Min Rooms')
    rooms_max = django_filters.NumberFilter(field_name='rooms', lookup_expr='lte', label='Max Rooms')

    class Meta:
        model = Maison
        fields = ['title', 'city', 'property', 'area', 'price', 'is_sold', 'rooms']
        
    # Méthode de filtre pour nettoyer les espaces dans le titre
    def filter_title(self, queryset, name, value):
        value = clean_spaces(value)  # Appliquer la normalisation des espaces
        return queryset.filter(**{name + '__icontains': value})

class TerrainFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Title')
    city = django_filters.CharFilter(lookup_expr='icontains', label='City')
    property = django_filters.ChoiceFilter(choices=[
        ('Maison', 'Maison'),
        ('Terrain', 'Terrain'),
        ('Appartement', 'Appartement')
    ], label='Property')
    area_min = django_filters.NumberFilter(field_name='area', lookup_expr='gte', label='Min Area')
    area_max = django_filters.NumberFilter(field_name='area', lookup_expr='lte', label='Max Area')
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Min Price')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Max Price')
    is_sold = django_filters.BooleanFilter(field_name='is_sold', label='Is Sold')

    class Meta:
        model = Terrain
        fields = ['title', 'city', 'property', 'area', 'price', 'is_sold']
        
    # Méthode de filtre pour nettoyer les espaces dans le titre
    def filter_title(self, queryset, name, value):
        value = clean_spaces(value)  # Appliquer la normalisation des espaces
        return queryset.filter(**{name + '__icontains': value})



import django_filters
from .models import Client

class ClientFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    phone = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone']




import django_filters
from .models import Transaction

class TransactionFilter(django_filters.FilterSet):
    client = django_filters.NumberFilter(field_name='client__id', lookup_expr='exact')  # Filtrer par ID du client
    property_type = django_filters.ChoiceFilter(choices=Transaction.PROPERTY_TYPE_CHOICES)
    transaction_type = django_filters.ChoiceFilter(choices=Transaction.TRANSACTION_TYPE_CHOICES)
    transaction_date = django_filters.DateFilter(lookup_expr='exact')  # Filtrer par date exacte
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')  # Filtrer par prix minimum
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')  # Filtrer par prix maximum

    class Meta:
        model = Transaction
        fields = ['client', 'property_type', 'transaction_type', 'transaction_date', 'price_min', 'price_max']
