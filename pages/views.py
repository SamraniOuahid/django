from django.shortcuts import render
from .models import Male

# Create your views here.
def index(request):
    # Récupérer les objets Male, en excluant ceux avec enfant = 0
    name = Male.objects.exclude(enfant=0)
    
    # Passer les objets directement au template (pas besoin de les convertir en chaîne)
    context = {'name': name}
    return render(request, 'pages/index.html', context)

def pages(request):
    return render(request, 'pages/about.html', {'n1': 'ouahid'})
