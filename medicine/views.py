from django.shortcuts import render, redirect
from .models import Profile, Supplier, Medicine, Donating, Purchasing, Prescription


# Create your views here.



def welcome(request):

		return render(request, 'test.html')


