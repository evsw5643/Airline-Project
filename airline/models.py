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