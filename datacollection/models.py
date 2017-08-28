from __future__ import unicode_literals
import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Drink(models.Model):
    """
    Model class that holds all data of all
    cocacola drinks
    """
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    flavor = models.CharField(max_length=50, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s" % self.name


class Data(models.Model):
    """
    Model class that holds all data collected,
    by data collectors
    """
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    collector = models.ForeignKey(User, related_name="collected_by",
                                  on_delete=models.CASCADE)
    consumer_name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    location_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    location_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    favorite_drink = models.ForeignKey(Drink, related_name="fav_drink",
                                       on_delete=models.CASCADE)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "data"

    def __unicode__(self):
        return "%s - %s, %s" % (
            self.collector.email,
            self.favorite_drink.name,
            self.location
        )
