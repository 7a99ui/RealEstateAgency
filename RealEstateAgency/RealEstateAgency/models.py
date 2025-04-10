from django.db import models

# Modèle Appartement
class Appartement(models.Model):
    id = models.BigAutoField(primary_key=True)

    title = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    property = models.CharField(max_length=50, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    rooms = models.IntegerField(blank=True, null=True)
    price = models.BigIntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    is_sold = models.BooleanField(default=False)

    class Meta:
        managed = False  # Keep it False if the table is already created; True if Django should manage the table
        db_table = 'appartement'
        app_label = 'RealEstateAgency'
        
    def clean(self):
        # Nettoyer les espaces multiples dans le titre
        if self.title:
            self.title = ' '.join(self.title.split()).strip()
        super().clean()  # Appel de la méthode clean() du parent pour toute validation supplémentaire

    def save(self, *args, **kwargs):
        self.full_clean()  # Assure que le nettoyage est effectué avant la sauvegarde
        super().save(*args, **kwargs)


# Modèle Maison
class Maison(models.Model):
    id = models.BigAutoField(primary_key=True)

    title = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    property = models.CharField(max_length=50, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    rooms = models.IntegerField(blank=True, null=True)
    price = models.BigIntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    is_sold = models.BooleanField(default=False)

    class Meta:
        managed = False  # Keep it False if the table is already created; True if Django should manage the table
        db_table = 'maison'
        app_label = 'RealEstateAgency'
        
    def clean(self):
        # Nettoyer les espaces multiples dans le titre
        if self.title:
            self.title = ' '.join(self.title.split()).strip()
        super().clean()  # Appel de la méthode clean() du parent pour toute validation supplémentaire

    def save(self, *args, **kwargs):
        self.full_clean()  # Assure que le nettoyage est effectué avant la sauvegarde
        super().save(*args, **kwargs)


# Modèle Terrain
class Terrain(models.Model):
    id = models.BigAutoField(primary_key=True)

    title = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    property = models.CharField(max_length=50, blank=True, null=True)
    area = models.FloatField(blank=True, null=True)
    price = models.BigIntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    is_sold = models.BooleanField(default=False)

    class Meta:
        managed = False  # Keep it False if the table is already created; True if Django should manage the table
        db_table = 'terrain'
        app_label = 'RealEstateAgency'
        
    def clean(self):
        # Nettoyer les espaces multiples dans le titre
        if self.title:
            self.title = ' '.join(self.title.split()).strip()
        super().clean()  # Appel de la méthode clean() du parent pour toute validation supplémentaire

    def save(self, *args, **kwargs):
        self.full_clean()  # Assure que le nettoyage est effectué avant la sauvegarde
        super().save(*args, **kwargs)



#client et transaction models




class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    
    class Meta:
        db_table = 'client'  # Nom de la table sans préfixe

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('achat', 'Achat'),
        ('vente', 'Vente'),
    ]

    PROPERTY_TYPE_CHOICES = [
        ('maison', 'Maison'),
        ('terrain', 'Terrain'),
        ('appartement', 'Appartement'),
    ]

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='transactions')
    property_id = models.IntegerField()  # ID de la propriété (Maison, Terrain ou Appartement)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE_CHOICES)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    transaction_date = models.DateField()
    price = models.FloatField()
    class Meta:
     db_table = 'transaction'  # Nom de la table sans préfixe

    def __str__(self):
        return f"Transaction {self.id} - {self.transaction_type}"

