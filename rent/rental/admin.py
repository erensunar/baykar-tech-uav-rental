from django.contrib import admin
from .models import Rental

class RentalAdmin(admin.ModelAdmin):
    list_display = ('renter', 'uav', 'rental_start_date', 'rental_end_date')
    list_filter = ('rental_start_date', 'rental_end_date')
    search_fields = ('renter__username', 'uav__model')

admin.site.register(Rental, RentalAdmin)