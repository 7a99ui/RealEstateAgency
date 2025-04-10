from django.contrib import admin
from .models import Appartement, Maison, Terrain , Client , Transaction

# Register models with the admin site
admin.site.register(Appartement)
admin.site.register(Maison)
admin.site.register(Terrain)
admin.site.register(Client)
admin.site.register(Transaction)
