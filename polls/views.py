from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Personne

# Create your views here.
def index(request):
    nom=request.POST['nom']
    prenom=request.POST['prenom']
    age=request.POST['age']
    
    personne=Personne(3,nom,prenom,age)
    personne.save()
    
    print('La méthode de requête est : ', nom)
    empl=Personne.objects.all
    return render(request, "index.html",{
        'empl':empl
        })
