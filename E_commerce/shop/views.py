from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def gallery(request):
    return render(request, 'gallery.html')


def products(request):
    return render(request, 'products.html')