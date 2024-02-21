from django.urls import path
from . import views

urlpatterns = [
    path('rental/<int:uav_id>/', views.rental_function, name='rental_function'),
]
