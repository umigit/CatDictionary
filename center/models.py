from django.db import models

class CatData(models.Model):
    created_date = models.DateTimeField('date published')
    latitude = models.FloatField()
    longitude = models.FloatField()
