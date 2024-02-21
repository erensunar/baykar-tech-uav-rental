from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404
from .models import UAV
# Create your views here.


def home_page(request):
    uavs = UAV.objects.all()
    context = {
        "uavs": uavs
    }
    return render(request, 'index.html', context)

def index(request):
    uavs = UAV.objects.all()
    context = {
        "uavs": uavs
    }
    return render(request, 'uavs/list.html', context)

def detail(request,uav_id):

    uav = get_object_or_404(UAV, pk=uav_id)
    context = {
        "uav": uav
    }
    return render(request, 'uavs/detail.html',context)

def search(request):
    return render(request, 'uavs/search.html')


