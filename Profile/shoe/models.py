from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Shoe(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    size = models.CharField(max_length=200)
    type = models.CharField(max_length=4)
    gender = models.CharField(max_length=1,null=True)
    photo = models.ImageField(null=True)

    def __str__(self):
        return self.name