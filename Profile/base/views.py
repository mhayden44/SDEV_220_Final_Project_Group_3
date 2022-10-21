from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, "home.html")

def mens(request):
	return render(request, "mens.html")

def womens(request):
	return render(request, "womens.html")
