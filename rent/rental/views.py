from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Rental
from uav_.models import UAV
from django.contrib import messages
from datetime import datetime
from django.utils.timezone import make_aware

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
    #Disable rent button if UAV is already rented
    # else:
    #     messages.add_message(request, messages.WARNING, "This UAV has already been rented.")
    #     return redirect('index')  # Redirect to home page if UAV is already rented



@login_required
def my_rentals(request):
    rentals = Rental.objects.filter(renter=request.user)
    for rental in rentals:
        # Anlık tarihi al
        current_datetime = timezone.now()
        # Kiralamanın bitiş tarihini bir datetime nesnesine dönüştür
        rental_end_datetime = make_aware(datetime.combine(rental.rental_end_date, datetime.min.time()))
        # Kalan günleri hesapla
        remaining_days = (rental_end_datetime - current_datetime).days
        # rental nesnesine kalan günleri ekle
        rental.remaining_days = remaining_days

    context = {
        'rentals': rentals
    }
    return render(request, 'rentals/my_rentals.html', context)
            

def cancel_rental(request, rental_id):
    rental = Rental.objects.get(id=rental_id)
    rental.delete()
    return redirect('my_rentals')  # veya başka bir URL'ye yönlendirme yapın