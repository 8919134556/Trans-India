from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views 


urlpatterns = [
     path('captain-login', views.captain_login, name='captain_login'),
     path('captain-feedback', views.captain_feedback, name='captain_feedback'),
     path('captain-home', views.captain_home, name='captain_home'),
     path('captain-order1', views.captain_order1, name='captain_order1'),
     path('captain-order/<int:id>', views.captain_order, name='captain_order'),
     
     path('captain-profile', views.captain_profile, name='captain_profile'),
     path('captain-register', views.captain_register, name='captain_register'),
     path('route', views.route, name="route"),
     
     path('base', views.base, name="base"),
     path('order', views.order, name="order"),
     path('ride/<int:id>/<str:email>/<str:c_id>/<str:c_na>', views.ride, name="ride"),
     

     
    
    
]