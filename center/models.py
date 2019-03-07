from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Cat(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Image(models.Model):
    cat = models.ForeignKey(Cat, on_delete=models.SET_NULL, null=True, related_name="images")
    image_original = models.ImageField(upload_to="images/")
    image_middle = ImageSpecField(source="image_original", processors=[ResizeToFill(800,600)], format="jpeg")
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
