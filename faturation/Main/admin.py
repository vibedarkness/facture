from django.contrib import admin

from .models import * 

# Register your models here.

class AdminClient(admin.ModelAdmin):
    list_display=('nom','email','telephone','adresse','age','sexe','ville')

    
class AdminFacture(admin.ModelAdmin):
    list_display = ('client','user','date_heure_facture','total','dernier_modification','statut','type_facture')


class AdminProduit(admin.ModelAdmin):
    list_display = ('facture','nom','quantite','prix','total')


admin.site.register(Client,AdminClient)
admin.site.register(Facture,AdminFacture)
admin.site.register(Produit,AdminProduit)
