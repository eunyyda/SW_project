from django.shortcuts import render, redirect
from .forms import UserForm, LocationForm
from .models import User, Location

def create_user_and_location(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        location_form = LocationForm(request.POST)
        if user_form.is_valid() and location_form.is_valid():
            user = user_form.save()
            location = location_form.save(commit=False)
            location.user = user
            location.save()
            return redirect('location_list')
    else:
        user_form = UserForm()
        location_form = LocationForm()
    return render(request, 'template/create_user_and_location.html', {
        'user_form': user_form,
        'location_form': location_form
    })


from .models import WeatherRecord
from .forms import WeatherRecordForm

def add_weather_record(request, location_id):
    location = Location.objects.get(id=location_id)
    if request.method == 'POST':
        form = WeatherRecordForm(request.POST)
        if form.is_valid():
            weather_record = form.save(commit=False)
            weather_record.location = location
            weather_record.save()
            return redirect('weather_record_list')
    else:
        form = WeatherRecordForm()
    return render(request, 'template/add_weather_record.html', {'form': form, 'location': location})