from rest_framework import serializers
from .models import Maison, Appartement, Terrain , Client , Transaction

# Serializer pour le modèle Maison
class MaisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maison
        fields = ['id', 'title', 'city', 'property', 'area', 'rooms', 'price', 'longitude', 'latitude', 'link' ,'is_sold']

# Serializer pour le modèle Appartement
class AppartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appartement
        fields = ['id', 'title', 'city', 'property', 'area', 'rooms', 'price', 'longitude', 'latitude', 'link' ,'is_sold']

# Serializer pour le modèle Terrain
class TerrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Terrain
        fields = ['id', 'title', 'city', 'property', 'area', 'price', 'longitude', 'latitude', 'link','is_sold']


# Serializer pour le modèle client
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'address']
        

# Serializer pour le modèle Transaction
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'client', 'property_id', 'property_type', 'transaction_type', 'transaction_date', 'price']