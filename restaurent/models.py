from django.db import models

class Table(models.Model):
    table = models.CharField(max_length=100)
    time = models.TimeField()
    date = models.DateField()
    accomodation = models.IntegerField()

    def __str__(self):
        return self.table
