from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
def login(request):
  
    return render(request, 'templates/login.html')

def home(request):
  

    return render(request, 'templates/homePage.html')

