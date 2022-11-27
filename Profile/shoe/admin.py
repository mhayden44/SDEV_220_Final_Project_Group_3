from django.contrib import admin
from .models import Category, Gender, Shoe, Customer


# Register your models here.
admin.site.register(Category)
admin.site.register(Gender)
admin.site.register(Shoe)
admin.site.register(Customer)