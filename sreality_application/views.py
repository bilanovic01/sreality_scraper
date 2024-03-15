from django.shortcuts import render
from .models import Flat

def index(request):
    items = Flat.objects.all()[:500]
    return render(request, 'index.html', {'items': items})
