from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def trace(request):
    return render(request, 'templates/login.html')

def home(request):
    return render(request, 'templates/homePage.html')
