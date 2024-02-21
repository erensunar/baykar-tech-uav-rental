from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Rental
from uav_.models import UAV
from django.contrib import messages

@login_required
def rental_function(request, uav_id):
    uav = get_object_or_404(UAV, pk=uav_id)
    if not uav.is_rented:
        rental_start_date = timezone.now()
        rental_end_date = rental_start_date + timezone.timedelta(days=30)
        rental = Rental.objects.create(renter=request.user, uav=uav, rental_start_date=rental_start_date, rental_end_date=rental_end_date)
        uav.is_rented = True
        uav.save()
        messages.add_message(request, messages.SUCCESS,'Rental completed.')
        return redirect('index')  # Redirect to home page if rental is successful
    else:
        messages.add_message(request, messages.WARNING, "This UAV has already been rented.")
        return redirect('index')  # Redirect to home page if UAV is already rented


            