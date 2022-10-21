
from django.urls import path
from . import views
  
urlpatterns = [
    path("", views.home, name="home"),
    path("mens/", views.mens, name="mens"),
    path("womens/", views.womens, name="womens"),
]