from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from uav_.models import UAV

class Rental(models.Model):
    renter = models.ForeignKey(User, on_delete=models.CASCADE)
    uav = models.ForeignKey(UAV, on_delete=models.CASCADE)
    rental_start_date = models.DateTimeField(default=timezone.now)  # Set the start date to the current date and time by default
    rental_end_date = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=30))  # Set the end date to 30 days from today by default

    def __str__(self):
        return f"{self.renter.username} - {self.uav.model} - {self.rental_start_date} to {self.rental_end_date}"
