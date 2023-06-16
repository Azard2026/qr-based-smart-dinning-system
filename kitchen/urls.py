from django.urls import path
from .  import views

app_name = 'kitchen'



urlpatterns = [
    path('login', views.login, name="login"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('completedorder',views.completedorder,name="completedorder"),

]
