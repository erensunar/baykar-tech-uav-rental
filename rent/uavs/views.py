from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import UAV
# Create your views here.

def index(request):
    return render(request, "uavs/list.html")

def detail(request):
    
    return render(request, 'uavs/detail.html')

def search(request):
    return render(request, 'uavs/search.html')