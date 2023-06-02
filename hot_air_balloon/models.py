from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Pilot(models.Model):
    ROLE_CHOICES = [
        ('Pilot', 'Pilot'),
        ('Co-pilot', 'Co-pilot'),
        ('Navigator', 'Navigator'),
        ('Flight Attendant', 'Flight Attendant'),
    ]
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    year_of_birth = models.IntegerField()
    total_hours = models.IntegerField()
    role = models.CharField(max_length=255, choices=ROLE_CHOICES)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Balloon(models.Model):
    TYPE_CHOICES = [
        ('Hot Air Balloon', 'Hot Air Balloon'),
        ('Helium Balloon', 'Helium Balloon'),
        ('Hydrogen Balloon', 'Hydrogen Balloon'),
    ]
    max_passengers = models.IntegerField()
    type = models.CharField(max_length=255, choices=TYPE_CHOICES)
    manufacturer = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.manufacturer} {self.type}'


class Airline(models.Model):
    name = models.CharField(max_length=255)
    year_founded = models.IntegerField()
    coverage_EU = models.BooleanField()

    def __str__(self):
        return f'{self.name}'


class AirlinePilot(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.pilot} {self.airline}'


class Flight(models.Model):
    code = models.CharField(max_length=255)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    balloon = models.ForeignKey(Balloon, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/')
    takeoff_airport = models.CharField(max_length=255)
    landing_airport = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.code}'

