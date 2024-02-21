from django.urls import path
from . import views

urlpatterns = [
    path('rental/<int:uav_id>/', views.rental_function, name='rental_function'),
    path('my_rentals/', views.my_rentals, name='my_rentals'),
    path('cancel_rental/<int:rental_id>/', views.cancel_rental, name='cancel_rental'),
]
