from django.urls import path
from .  import views

app_name = 'food'

urlpatterns = [
    path('menu', views.menu, name="menu"),
    path('cart', views.cart, name="cart"),
    path('order', views.order, name='order'),
    path('success', views.success, name='success'),
    path('payment',views.payment,name="payment"),
     path('card',views.card,name="card"),
    # path('call',views.calltable,name="call")
    
]
