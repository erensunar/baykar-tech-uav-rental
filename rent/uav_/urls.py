from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='uavs'),
    path('<int:uav_id>', views.detail, name='detail'),
    path('search', views.search, name='search'),
    path("", views.home_page, name= "index")
]

