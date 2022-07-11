"""listify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from listapp import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    
    #Auth
    path('signup/', views.signupuser, name='signupuser'), 
    path('login/', views.loginuser, name='loginuser'), 
    path('logout/', views.logoutuser, name='logoutuser'), 
           
    #Listify 
    path('', views.home, name='home'),
    path('create/', views.createnote, name='createnote'),  
    path('current/', views.currentnotes, name='currentnotes'),
    path('completed/', views.completednotes, name='completednotes'),
    path('note/<int:note_pk>', views.viewnote, name='viewnote'),
    path('note/<int:note_pk>/complete', views.completenote, name='completenote'),   
    path('note/<int:note_pk>/delete', views.deletenote, name='deletenote'),       
             
    
]
