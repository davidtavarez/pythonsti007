from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Vehicle(models.Model):
    manufacturer = models.CharField(max_length=20)
    model = models.CharField(max_length=10)
    year = models.PositiveSmallIntegerField()

    TYPE_CHOICES = (
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Compact', 'Compact'),
        ('Sport', 'Sport')
    )

    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default="Sedan")
    plate = models.CharField(max_length=15)

    created_at = models.DateTimeField(editable=False, default=timezone.now)

    def __unicode__(self):
        return self.plate

    class Meta:
        ordering = ('plate',)


class Employee(models.Model):
    user = models.ForeignKey('auth.User', )
    name = models.CharField(max_length=30, default="", verbose_name="name")
    phone_number = models.CharField(max_length=16)
    vehicle = models.ForeignKey(Vehicle)
    created_at = models.DateTimeField(editable=False, default=timezone.now)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Crater(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=18.735693, verbose_name="Latitude")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=-70.162651,
                                    verbose_name="Longitude")
    nickname = models.CharField(max_length=30, default="", verbose_name="nickname")
    reported_by = models.ForeignKey(Employee)
    discovered_at = models.DateTimeField(editable=False, default=timezone.now)

    def __unicode__(self):
        return self.nickname

    class Meta:
        ordering = ('nickname',)


class Fall(models.Model):
    employee = models.ForeignKey(Employee)
    crater = models.ForeignKey(Crater)
    fallen_at = models.DateTimeField(editable=False, default=timezone.now)

    def __unicode__(self):
        return self.crater

    class Meta:
        ordering = ('-fallen_at',)