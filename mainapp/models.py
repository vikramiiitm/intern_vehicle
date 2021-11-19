from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Navigation(models.Model):

    class Engine(models.TextChoices):
        GOOD = "Good"
        BAD ="Bad"

    class Fuel(models.TextChoices):
        FULL = "Full"
        HALF = "Half"
        EMPTY = "Empty"
    map = models.CharField(max_length=255,blank=True,null=True)
    vehicle_name = models.CharField(max_length=200)
    speed = models.IntegerField(blank=True,null=True)
    avg_speed = models.IntegerField(blank=True,null=True)
    temprature = models.IntegerField(blank=True,null=True)
    fuel = models.CharField(_('Fuel'),max_length=255,choices=Fuel.choices, default=Fuel.FULL)
    engine = models.CharField(_('Engine'),max_length=255,choices=Fuel.choices, default=Engine.GOOD)

