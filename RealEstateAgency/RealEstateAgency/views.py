from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view , action
from rest_framework import viewsets, filters
from .models import Maison, Appartement, Terrain ,Client ,Transaction
from .serializers import MaisonSerializer, AppartementSerializer, TerrainSerializer , ClientSerializer , TransactionSerializer
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MaisonFilter, AppartementFilter, TerrainFilter , ClientFilter , TransactionFilter # Assurez-vous d'ajouter vos filtres
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.filters import OrderingFilter



@api_view(['GET'])
def search_maisons(request):
    queryset = Maison.objects.all()

    # Filtrage par surface minimale
    area_min = request.GET.get('area_min')
    if area_min:
        queryset = queryset.filter(area__gte=area_min)

    # Filtrage par surface maximale
    area_max = request.GET.get('area_max')
    if area_max:
        queryset = queryset.filter(area__lte=area_max)

    # Filtrage par ville (en ignorant les espaces et insensible à la casse)
    city = request.GET.get('city')
    if city:
        queryset = queryset.filter(city__icontains=city.strip())  # Suppression des espaces et insensibilité à la casse

    # Filtrage par prix minimal
    price_min = request.GET.get('price_min')
    if price_min:
        queryset = queryset.filter(price__gte=price_min)

    # Filtrage par prix maximal
    price_max = request.GET.get('price_max')
    if price_max:
        queryset = queryset.filter(price__lte=price_max)

    # Filtrage par nombre de chambres
    rooms = request.GET.get('rooms')
    if rooms:
        queryset = queryset.filter(rooms=rooms)
    
     # Filtrage par état de vente (is_sold)
    is_sold = request.GET.get('is_sold')
    if is_sold is not None:
        queryset = queryset.filter(is_sold=is_sold.lower() == 'true')  # Convertir en booléen

    # Sérialisation des données filtrées
    serializer = MaisonSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_maison(request):
    """
    Crée une nouvelle maison avec les données fournies.
    """
    serializer = MaisonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_maison(request, pk):
    """
    Récupère une maison spécifique par son ID.
    """
    maison = Maison.objects.filter(pk=pk).first()
    if not maison:
        return Response({'error': 'Maison non trouvée'}, status=status.HTTP_404_NOT_FOUND)

    serializer = MaisonSerializer(maison)
    return Response(serializer.data)

@api_view(['PATCH'])
def update_maison(request, pk):
    """
    Modifie une maison existante par son ID.
    """
    maison = Maison.objects.filter(pk=pk).first()
    if not maison:
        return Response({'error': 'Maison non trouvée'}, status=status.HTTP_404_NOT_FOUND)

    serializer = MaisonSerializer(maison, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_maison(request, pk):
    """
    Supprime une maison existante par son ID.
    """
    maison = Maison.objects.filter(pk=pk).first()
    if not maison:
        return Response({'error': 'Maison non trouvée'}, status=status.HTTP_404_NOT_FOUND)

    maison.delete()
    return Response({'message': 'Maison supprimée avec succès'}, status=status.HTTP_204_NO_CONTENT)




#appartement

@api_view(['GET'])
def search_appartements(request):
    queryset = Appartement.objects.all()

    # Filtrage par surface minimale
    area_min = request.GET.get('area_min')
    if area_min:
        queryset = queryset.filter(area__gte=area_min)

    # Filtrage par surface maximale
    area_max = request.GET.get('area_max')
    if area_max:
        queryset = queryset.filter(area__lte=area_max)

    # Filtrage par ville
    city = request.GET.get('city')
    if city:
        queryset = queryset.filter(city__icontains=city.strip())  # Suppression des espaces au début et à la fin

    # Filtrage par prix minimal
    price_min = request.GET.get('price_min')
    if price_min:
        queryset = queryset.filter(price__gte=price_min)

    # Filtrage par prix maximal
    price_max = request.GET.get('price_max')
    if price_max:
        queryset = queryset.filter(price__lte=price_max)

    # Filtrage par nombre de chambres
    rooms = request.GET.get('rooms')
    if rooms:
        queryset = queryset.filter(rooms=rooms)

    # Filtrage par état de vente (is_sold)
    is_sold = request.GET.get('is_sold')
    if is_sold is not None:
        queryset = queryset.filter(is_sold=is_sold.lower() == 'true')  # Convertir en booléen

    # Sérialisation des données filtrées
    serializer = AppartementSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_appartement(request):
    """
    Crée une nouvelle maison avec les données fournies.
    """
    serializer = AppartementSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_appartement(request, pk):
    """
    Récupère une maison spécifique par son ID.
    """
    appartement = Appartement.objects.filter(pk=pk).first()
    if not appartement:
        return Response({'error': 'Appartement non trouvée'}, status=status.HTTP_404_NOT_FOUND)

    serializer = MaisonSerializer(appartement)
    return Response(serializer.data)



@api_view(['PATCH'])
def update_appartement(request, pk):
    """
    Modifie une appartement existante par son ID.
    """
    appartement = Appartement.objects.filter(pk=pk).first()
    if not appartement:
        return Response({'error': 'Appartement non trouvée'}, status=status.HTTP_404_NOT_FOUND)

    serializer = MaisonSerializer(appartement, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_appartement(request, pk):
    """
    Supprime une maison existante par son ID.
    """
    appartement = Appartement.objects.filter(pk=pk).first()
    if not appartement:
        return Response({'error': 'Appartement non trouvée'}, status=status.HTTP_404_NOT_FOUND)

    appartement.delete()
    return Response({'message': 'Appartement supprimée avec succès'}, status=status.HTTP_204_NO_CONTENT)

#terrain
@api_view(['GET'])
def search_terrains(request):
    queryset = Terrain.objects.all()

    # Filtrage par ville (insensible aux espaces et insensibilité à la casse)
    city = request.GET.get('city')
    if city:
        queryset = queryset.filter(city__icontains=city.strip())  # Enlève les espaces et ignore la casse

    # Filtrage par surface minimale
    area_min = request.GET.get('area_min')
    if area_min:
        queryset = queryset.filter(area__gte=area_min)

    # Filtrage par surface maximale
    area_max = request.GET.get('area_max')
    if area_max:
        queryset = queryset.filter(area__lte=area_max)

    # Filtrage par prix minimal
    price_min = request.GET.get('price_min')
    if price_min:
        queryset = queryset.filter(price__gte=price_min)

    # Filtrage par prix maximal
    price_max = request.GET.get('price_max')
    if price_max:
        queryset = queryset.filter(price__lte=price_max)

    # Filtrage par état de vente (is_sold)
    is_sold = request.GET.get('is_sold')
    if is_sold is not None:
        queryset = queryset.filter(is_sold=is_sold.lower() == 'true')  # Convertir en booléen

    # Sérialisation des données filtrées
    serializer = TerrainSerializer(queryset, many=True)
    return Response(serializer.data)




@api_view(['POST'])
def create_terrain(request):
    """
    Crée une nouvelle maison avec les données fournies.
    """
    serializer = TerrainSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_terrain(request, pk):
    """
    Récupère une maison spécifique par son ID.
    """
    terrain = Terrain.objects.filter(pk=pk).first()
    if not terrain:
        return Response({'error': 'Terrain non trouvée'}, status=status.HTTP_404_NOT_FOUND)

    serializer = MaisonSerializer(terrain)
    return Response(serializer.data)

@api_view(['PATCH'])
def update_terrain(request, pk):
    """
    Modifie une terrain existante par son ID.
    """
    terrain = Terrain.objects.filter(pk=pk).first()
    if not terrain:
        return Response({'error': 'Terrain non trouvée'}, status=status.HTTP_404_NOT_FOUND)

    serializer = TerrainSerializer(terrain, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_terrain(request, pk):
    """
    Supprime une terrain existante par son ID.
    """
    terrain = Terrain.objects.filter(pk=pk).first()
    if not terrain:
        return Response({'error': 'Terrain non trouvée'}, status=status.HTTP_404_NOT_FOUND)

    terrain.delete()
    return Response({'message': 'Terrain supprimée avec succès'}, status=status.HTTP_204_NO_CONTENT)

from rest_framework import generics

# views.py
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .models import Terrain, Appartement, Maison
from .serializers import TerrainSerializer, AppartementSerializer, MaisonSerializer
from .filters import TerrainFilter, AppartementFilter, MaisonFilter

class TerrainListView(generics.ListAPIView):
    queryset = Terrain.objects.all()
    serializer_class = TerrainSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = TerrainFilter
    ordering_fields = ['price', 'area']  # Assurez-vous que 'price' et 'area' existent dans votre modèle Terrain
    ordering = ['price']  # Tri par défaut sur le prix

class AppartementListView(generics.ListAPIView):
    queryset = Appartement.objects.all()
    serializer_class = AppartementSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = AppartementFilter
    ordering_fields = ['price', 'area', 'rooms']  # Assurez-vous que 'price', 'area', et 'rooms' existent dans votre modèle Appartement
    ordering = ['price']  # Tri par défaut sur le prix

class MaisonListView(generics.ListAPIView):
    queryset = Maison.objects.all()
    serializer_class = MaisonSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_class = MaisonFilter
    ordering_fields = ['price', 'area', 'rooms']  # Assurez-vous que 'price', 'area', et 'rooms' existent dans votre modèle Maison
    ordering = ['price']  # Tri par défaut sur le prix


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Client
from .serializers import ClientSerializer
# Liste des clients avec filtrage via 'search'
@api_view(['GET'])
def search_clients(request):
    queryset = Client.objects.all()
    first_name = request.query_params.get('first_name')
    last_name = request.query_params.get('last_name')
    email = request.query_params.get('email')
    phone = request.query_params.get('phone')

    if first_name:
        queryset = queryset.filter(first_name__icontains=first_name)
    if last_name:
        queryset = queryset.filter(last_name__icontains=last_name)
    if email:
        queryset = queryset.filter(email__icontains=email)
    if phone:
        queryset = queryset.filter(phone__icontains=phone)

    serializer = ClientSerializer(queryset, many=True)
    return Response(serializer.data)


# Créer un client
@api_view(['POST'])
def create_client(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Récupérer un client par ID
@api_view(['GET'])
def get_client(request, id):
    client = get_object_or_404(Client, id=id)
    serializer = ClientSerializer(client)
    return Response(serializer.data)


# Mettre à jour un client
@api_view(['PATCH'])
def update_client(request, id):
    client = get_object_or_404(Client, id=id)
    serializer = ClientSerializer(client, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Supprimer un client
@api_view(['DELETE'])
def delete_client(request, id):
    client = get_object_or_404(Client, id=id)
    client.delete()
    return Response({"message": "Client deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

from .models import Transaction
from .serializers import TransactionSerializer

# Liste des transactions avec filtrage via 'search'
@api_view(['GET'])
def search_transactions(request):
    queryset = Transaction.objects.all()
    client = request.query_params.get('client')
    transaction_type = request.query_params.get('transaction_type')
    property_type = request.query_params.get('property_type')
    transaction_date = request.query_params.get('transaction_date')
    price_min = request.query_params.get('price_min')
    price_max = request.query_params.get('price_max')
    property_id = request.query_params.get('property_id')  # Retrieve property_id filter

    if client:
        queryset = queryset.filter(client__id=client)
    if transaction_type:
        queryset = queryset.filter(transaction_type=transaction_type)
    if property_type:
        queryset = queryset.filter(property_type=property_type)
    if transaction_date:
        queryset = queryset.filter(transaction_date=transaction_date)
    if price_min:
        queryset = queryset.filter(price__gte=price_min)
    if price_max:
        queryset = queryset.filter(price__lte=price_max)
    if property_id:
        queryset = queryset.filter(property_id=property_id)  # Filter by property_id

    serializer = TransactionSerializer(queryset, many=True)
    return Response(serializer.data)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction, Maison, Appartement, Terrain
from .serializers import TransactionSerializer
from datetime import date

@api_view(['POST'])
def create_transaction(request):
    client_id = request.data.get('client')
    property_id = request.data.get('property_id')
    property_type = request.data.get('property_type')

    # Définir transaction_type comme "achat"
    transaction_type = "achat"

    # Récupérer le modèle correspondant (Maison, Terrain ou Appartement)
    if property_type == "maison":
        property_model = Maison
    elif property_type == "terrain":
        property_model = Terrain
    elif property_type == "appartement":
        property_model = Appartement
    else:
        return Response({"error": "Invalid property type."}, status=status.HTTP_400_BAD_REQUEST)

    # Vérifier si la propriété existe et n'est pas vendue
    try:
        property_instance = property_model.objects.get(id=property_id, is_sold=False)
    except property_model.DoesNotExist:
        return Response({"error": "Property not available for transaction."}, status=status.HTTP_400_BAD_REQUEST)

    # Déterminer le prix de la propriété
    price = property_instance.price

    # Créer la transaction
    new_transaction = Transaction.objects.create(
        client_id=client_id,
        property_id=property_id,
        property_type=property_type,
        transaction_type=transaction_type,  # Toujours "achat"
        transaction_date=str(date.today()),  # Définir la date par défaut
        price=price
    )

    # Marquer la propriété comme vendue
    property_instance.is_sold = True
    property_instance.save()

    return Response({
        "message": "Transaction created successfully.",
        "transaction": {
            "id": new_transaction.id,
            "client": new_transaction.client.id,
            "property_id": new_transaction.property_id,
            "property_type": new_transaction.property_type,
            "transaction_type": new_transaction.transaction_type,
            "transaction_date": new_transaction.transaction_date,
            "price": new_transaction.price,
        }
    }, status=status.HTTP_201_CREATED)


# Récupérer une transaction par ID
@api_view(['GET'])
def get_transaction(request, id):
    transaction = get_object_or_404(Transaction, id=id)
    serializer = TransactionSerializer(transaction)
    return Response(serializer.data)


# Mettre à jour une transaction
@api_view(['PATCH'])
def update_transaction(request, id):
    transaction = get_object_or_404(Transaction, id=id)
    serializer = TransactionSerializer(transaction, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Supprimer une transaction
@api_view(['DELETE'])
def delete_transaction(request, id):
    transaction = get_object_or_404(Transaction, id=id)
    transaction.delete()
    return Response({"message": "Transaction deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
















from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status





class PropertyMapView(APIView):
    def get(self, request, property_type, property_id):
        try:
            # Vérifiez le type de propriété et récupérez l'objet correspondant
            if property_type == "maison":
                property = Maison.objects.get(id=property_id)
            elif property_type == "appartement":
                property = Appartement.objects.get(id=property_id)
            elif property_type == "terrain":
                property = Terrain.objects.get(id=property_id)
            else:
                return Response({"error": "Invalid property type"}, status=status.HTTP_400_BAD_REQUEST)
            
            # Générez l'URL Google Maps à partir de latitude et longitude
            map_url = f"https://www.google.com/maps?q={property.latitude},{property.longitude}"
            return Response({"map_url": map_url}, status=status.HTTP_200_OK)

        except (Maison.DoesNotExist, Appartement.DoesNotExist, Terrain.DoesNotExist):
            return Response({"error": "Property not found"}, status=status.HTTP_404_NOT_FOUND)
