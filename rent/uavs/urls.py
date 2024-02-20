from django.urls import path
from . import views


#127.0.0.1:8000

urlpatterns = [
    path('', views.index, name='uavs'),
    path('<int:uav_id>', views.detail, name='detail'),
    path('search', views.search, name='search'),
]

