from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    SEXE_TYPE=(
        ("M","Masculin"),
        ("F","Feminin"),
    )

    nom = models.CharField(max_length=150)
    email = models.EmailField()
    telephone = models.CharField(max_length = 150)
    adresse = models.CharField(max_length = 150)
    sexe = models.CharField(max_length = 1,choices=SEXE_TYPE)
    age = models.CharField(max_length = 12)
    ville = models.CharField(max_length = 150)
    created_at = models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.nom


class Facture(models.Model):
    Facture_Type=(
        ('Reçu','Reçu'),
        ('Proforma','Facture Proforma'),
        ('Facture','Facture')
    )

    client=models.ForeignKey(Client, on_delete=models.PROTECT)
    user=models.ForeignKey(User,on_delete=models.PROTECT)
    date_heure_facture=models.DateTimeField(auto_now_add=True)
    total = models.IntegerField()
    dernier_modification=models.DateTimeField(null=True, blank=True)
    statut = models.BooleanField(default=False)
    type_facture = models.CharField(max_length = 100, choices=Facture_Type)

    class Meta:
        verbose_name = 'Facture'
        verbose_name_plural = 'Factures'
        
    def __str__(self):
        return f'{self.client.nom} {self.date_heure_facture}'
    
    @property
    def get_total(self):
        produits=self.produit_set.all()   

        total=sum(produit.get_total for produit in produits) 

class Produit(models.Model):
    facture=models.ForeignKey(Facture, on_delete=models.PROTECT)
    nom = models.CharField(max_length = 150)
    quantite= models.IntegerField()
    # unite = models.CharField(max_length = 150, default="null", null=True)
    prix=models.IntegerField()
    total=models.IntegerField()

    class Meta:
        verbose_name = 'Produit'
        verbose_name_plural = 'Produits'

    def __str__(self):
        return 
    
    @property
    def get_total(self):

        total=self.prix * self.quantite

    
    
    
    
    