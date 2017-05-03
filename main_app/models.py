from django.db import models


class Treasure(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='treasure_images', default='media/default.png')
