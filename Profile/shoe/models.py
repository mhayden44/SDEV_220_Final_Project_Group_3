from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.utils import timezone

fs = FileSystemStorage(location='/media/photos')

# Create your models here.

class Category(models.Model):
    SHOE_TYPES=(
        ('ATHL', 'Athletic'),
        ('DRSS','Dress'),
        ('WORK','Work'),
        ('CASL','Casual'),
    )
    type = models.CharField(max_length=4,choices=SHOE_TYPES)

    @staticmethod
    def get_all_types():
        return Category.objects.all()

    def __str__(self):
        return self.type


class Gender(models.Model):
    GENDER_TYPES=(
        ('M','Male'),
        ('F','Female'),
    )
    gender = models.CharField(max_length=1,choices=GENDER_TYPES)
    
    @staticmethod
    def get_all_genders():
        return Gender.objects.all()

    def __str__(self):
        return self.gender


class Shoe(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=100,null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    size = models.CharField(max_length=200)
    type = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    # gender = models.CharField(max_length=1,null=True)
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE,default=1)
    photo = models.ImageField(storage=fs,null=True)

    @staticmethod
    def get_shoes_by_id(ids):
        return Shoe.objects.filter (id__in=ids)
    @staticmethod
    def get_all_shoes():
        return Shoe.objects.all()

    def __str__(self):
        return self.name
    


class Customer(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=200)

    def register(self):
        self.save()
    
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True
        else:
            return False