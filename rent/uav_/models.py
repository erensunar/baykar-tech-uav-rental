from django.db import models

class UAV(models.Model):
    branch = models.CharField(max_length=100, verbose_name="Branch")
    model = models.CharField(max_length=100, verbose_name="Model")
    weight = models.FloatField(max_length=10, verbose_name="Weight")
    category = models.CharField(max_length=100, verbose_name="Category")
    monthly_fee = models.FloatField(max_length=10, verbose_name="Monthly Fee")
    is_rented = models.BooleanField(default = False, verbose_name="is Rented")
    image = models.CharField(max_length=50, verbose_name="Image Path", default='')
    description = models.TextField( verbose_name = "Description")
    
    def __str__(self) -> str:
        return self.model
    
    def get_image_path(self):
        return "/img/"+ self.image