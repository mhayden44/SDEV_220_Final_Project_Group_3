from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.utils import timezone

fs = FileSystemStorage(location='/media/photos')

# Create your models here.

class Shoe(models.Model):
    SHOE_TYPES=(
        ('ATHL', 'Athletic'),
        ('DRSS','Dress'),
        ('WORK','Work'),
        ('CASL','Casual'),
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=100,null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    size = models.CharField(max_length=200)
    type = models.CharField(max_length=4, choices=SHOE_TYPES,null=True)
    gender = models.CharField(max_length=1,null=True)
    photo = models.ImageField(storage=fs,null=True)

    def __str__(self):
        return self.name
