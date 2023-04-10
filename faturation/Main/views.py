from django.shortcuts import render
from .models import *

from django.views import View

from django.contrib import messages

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
    
    def post(self,request, *args, **kwargs):
        return render(request,self.templates_name,self.context)
    
     

