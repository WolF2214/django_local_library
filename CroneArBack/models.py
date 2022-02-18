from django.db import models
from tkinter import CASCADE
from datetime import datetime

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name

class Marker(models.Model):
    STATUS_CHOICES = (
        ('CQB', 'CQB'),
        ('ASSAULT', 'ASSAULT'),
        ('SUPPORT', 'SUPPORT'),
        ('DMR', 'DMR'),
        ('SNIPER', 'SNIPER')
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)
    rol = models.CharField(choices=STATUS_CHOICES, max_length=30)
    fps = models.IntegerField()
    upload_date = models.DateField()