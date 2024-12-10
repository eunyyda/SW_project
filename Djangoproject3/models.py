from django.db import models


class User(models.Model):
    username = models.CharField(max_length=30)
    birth_date = models.DateField()
    email = models.EmailField(unique = True)
    location = models.CharField(max_length = 30)

    def __str__(self):
        return self.username

class Location(models.Model):
    user = models.ForeignKey(User,on_delte=models.CASCADE)
    city = models.CharField(max_length=30)
    country = models.DateField(max_length=30)

    def __str__(self):
        return f"{self.city}-{self.country}"

class WeatherRecord(models.Model):
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    date = models.DateField()
    temperature = models.Floatfield()
    condition = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.location.city} - {self.date} ({self.temperature}°C)"