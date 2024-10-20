"""
URL configuration for ods project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from  . import views
from .views import doctor_login_view, doctor_detail_view,login
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('signup/',views.signup,name='signup'),
    path('pledge/',views.pledge),
    path('login/', views.login, name='doctor_login'),
    path('doctor/view', doctor_detail_view, name='doctor_detail'),
    path('logout/', views.doctor_logout_view, name='logout'),  


    
]
