from django.shortcuts import render
from .baccarat.baccarat_cli import Cli

# Create your views here.
def home(request):
    return render(request, 'baccarat/index.html')