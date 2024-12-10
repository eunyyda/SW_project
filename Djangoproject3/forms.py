from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, Location, WeatherRecord

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['city', 'country']

class WeatherRecordForm(forms.ModelForm):
    class Meta:
        model = WeatherRecord
        fields = ['date', 'temperature', 'condition']