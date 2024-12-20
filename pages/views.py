from django.shortcuts import render
from .models import Male

# Create your views here.
def index(request):
    # Récupérer les objets Male, en excluant ceux avec enfant = 0
    name = Male.objects.all()
    
    # Passer les objets directement au template (pas besoin de les convertir en chaîne)
    x = {'name': name.filter(age = 32) }
    return render(request, 'pages/index.html', x)

def pages(request):
    return render(request, 'pages/about.html', {'n1': 'ouahid'})
