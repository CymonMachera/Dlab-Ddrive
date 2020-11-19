from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
def login(request):
    if request.session.has_key('user'):
        user = request.session['user']
        return redirect('/home')
    else:
        return render(request, 'templates/login.html')

def home(request):
    if request.session.has_key('user'):
        user = request.session['user']
        print(user)
        return render(request,  'templates/homePage.html', {"user" : user})
    else:
        return redirect('/login')

    # return render(request, 'templates/homePage.html')

def logout(request):
    try:
        del request.session['user']
    except:
        pass

    responsed = redirect('/login')
    return responsed