from ast import arg
from django.db import models

class Airplane(models.Model):
    def __str__(self):
        return self.airplane_name

    airplane_name = models.CharField(max_length=200)
    airplane_number = models.IntegerField(max_length=4)
    airplane_date_of_departure = models.DateTimeField("Departure date")


class User(models.Model):
    def __str__(self):
        return self.name


class Singleton(models.Model):
    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)


class Setting(Singleton):
    backgrounds = (
        ('poop.jpg', 'poop.jpg'),
        ('fuck.jpg', 'fuck.jpg'),
        ('bitch.png', 'bitch.png')
        )
    background_title = models.CharField(max_length=100, choices=backgrounds)