from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    facture=Facture.objects.all()

    context={
        'facture':facture,
    }

    return render(request,'index.html',context)
