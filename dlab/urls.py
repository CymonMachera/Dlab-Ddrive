"""dlab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from rest_framework_simplejwt import views as jwt_views
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('documentation/', include('documentation.urls')),
    path('login/', include('account.urls')),
    path('home/', include('home.urls')),
    path('program/', include('program.urls')),
    
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

admin.site.site_header = 'dLab DRIVE'
admin.site.site_title = 'dLab DRVIE Adminsitration' 
admin.site.index_title = 'Site Administration'                 # default: "Site administration"