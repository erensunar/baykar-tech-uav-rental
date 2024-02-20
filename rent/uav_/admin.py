from django.contrib import admin
from .models import UAV
# Register your models here.

class UAV_Admin(admin.ModelAdmin):
    list_display = ("id", "branch", "model", "weight", "category", "monthly_fee", "is_rented" ,)
    list_display_links = ("id",)
    list_filter = ("branch", "model","category", "is_rented",)
    list_editable = ("is_rented", )
    search_fields = ("branch","model",)
    list_per_page = 10


admin.site.register(UAV, UAV_Admin)