from django.shortcuts import render
from main_app.models import Treasure

def index(request):
    treasures = Treasure.objects.all()
    return render(request, 'index.html', {'treasures':treasures})
