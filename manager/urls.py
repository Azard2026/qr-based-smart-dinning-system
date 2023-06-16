from django.urls import path
from django.contrib import admin
from .  import views

app_name = 'manager'

urlpatterns = [
     path('admin/', admin.site.urls,name="admin"),
     path('index', views.index, name="index"),
     path('dashboard',views.dashboard,name="dashboard"),
     path('conformorder',views.conformorder,name="conformorder"),
     path('summary',views.summary,name="summary"),
     path('qrgenerator',views.qrgenerator,name="qrgenerator"),
     path('logout',views.logOut,name="logout"),
   
]
