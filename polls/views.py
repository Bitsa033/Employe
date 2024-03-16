from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from polls.models import Personne

# Create your views here.
def index(request):
    
    empl=Personne.objects.all
    
    return render(request, "employe/index.html",{
        'empl':empl
        })
    
def addEmpl(request):
        
    nom = request.POST.get('nom')
    prenom = request.POST.get('prenom')
    age = request.POST.get('age')
        
    if request.method == "POST":
            
        pers=Personne(nom=nom,prenom=prenom,age=age)
        pers.save()
    
        print('La méthode de requête est : ', nom)
        return HttpResponseRedirect("/")
        
    return render(request, "employe/new.html")

def show(request,id):
    
    empl=Personne.objects.get(id=id)
    
    return render(request, "employe/show.html",{
        'empl':empl
        })
        
        
