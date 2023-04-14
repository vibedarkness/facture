from django.shortcuts import render
from .models import *

from django.views import View

from django.contrib import messages
from django.db import transaction

# Create your views here.

# def index(request):
#     facture=Facture.objects.all()

#     context={
#         'facture':facture,
#     }

#     return render(request,'index.html',context)

class IndexView(View):

    templates_name="index.html"
    facture=Facture.objects.select_related('client','user').all()
    context={
        'facture':facture,
    }

    def get(self,request, *args, **kwargs):
        return render(request,self.templates_name,self.context)
    
    def post(self,request, *args, **kwargs):
        return render(request,self.templates_name,self.context)
    


class ClientView(View):
    templates_name='add_client.html'
    
    def get(self,request, *args, **kwargs):
        return render(request,self.templates_name)
    
    def post(self,request, *args, **kwargs):
        value={
            'nom':request.POST.get('nom'),
            'email':request.POST.get('email'),
            'telephone':request.POST.get('telephone'),
            'adresse':request.POST.get('adresse'),
            'sexe':request.POST.get('sexe'),
            'age':request.POST.get('age'),
            'ville':request.POST.get('ville'),
            'user':request.user
        }

        try:
            create_client=Client.objects.create(**value)
            if create_client:
                messages.success(request, "client ajouter avec success")
            else:
                messages.error(request,"Erreur lors de l'enregistrement du client veuillez reéssayé svp")    

        except Exception as e:
            messages.error(request,f'desolé nous avons rencontrer un probleme de : {e}')

        return render(request,self.templates_name)
    
    


class FactureView(View):
    templates_name="add_facture.html" 

    clients=Client.objects.select_related('user').all()



    context={
        'clients':clients
    }


    
    def get(self,request, *args, **kwargs):
        return render(request,self.templates_name,self.context)
    
    @transaction.atomic()
    def post(self, request, *args, **kwargs):
            
            items = []

            try: 

                client = request.POST.get('client')

                type = request.POST.get('type')

                noms = request.POST.getlist('nom')

                # unite = request.POST.getlist('unite')

                quantite = request.POST.getlist('quantite')

                prix = request.POST.getlist('prix')

                total_a = request.POST.getlist('total-a')

                total = request.POST.get('total')

                facture_object = {
                    'client_id': client,
                    'user': request.user,
                    'total': total,
                    'type_facture': type,

                }

                facture = Facture.objects.create(**facture_object)

                for i, nom in enumerate(noms):
                    data= Produit(
                        facture_id=facture.id,
                        nom=nom,
                        quantite=quantite[i],
                        prix=prix[i],
                        total=total_a

                    )

                    items.append(data)
                created = Produit.objects.bulk_create(items) 
                if created:
                    messages.success(request, "Data saved successfully.") 
                else:
                    messages.error(request, "Sorry, please try again the sent data is corrupt.")       
            except Exception as e:
                messages.error(request, f"Sorry the following error has occured {e}.")   

            return  render(request, self.templates_name, self.context)
        
        

