from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from employe.models import Personne

# Create your views here.
def index(request):
    
    empl=Personne.objects.all
    
    return render(request, "employe/index.html",{
        'empl':empl
        })
    
def addEmpl(request):
        
    return render(request, "employe/new.html")

def storeEmpl(request):
        
    nom = request.POST.get('nom')
    prenom = request.POST.get('prenom')
    age = request.POST.get('age')
        
    if request.method == "POST":
            
        pers=Personne(nom=nom,prenom=prenom,age=age)
        pers.save()
    
        print('La méthode de requête est : ', nom)
        return HttpResponseRedirect("/")

def showEmpl(request,id):
    
    empl=Personne.objects.get(id=id)
    
    return render(request, "employe/show.html",{
        'empl':empl
        })

def updateEmpl(request,id):
    
    nom = request.POST.get('nom')
    prenom = request.POST.get('prenom')
    age = request.POST.get('age')
    empl=Personne.objects.get(id=id)
    if request.method == "POST":
        empl.nom=nom
        empl.prenom=prenom
        empl.age=age
        empl.save()
        return HttpResponseRedirect("/")
    
def deleteEmpl(request,id):
    
    empl=Personne.objects.get(id=id)
    empl.delete()
    return HttpResponseRedirect("/")
    
    
        
        
