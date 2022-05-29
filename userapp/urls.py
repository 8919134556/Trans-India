from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views 
urlpatterns = [
    path('user-booking', views.user_booking, name='user_booking'),
    path('user-home', views.user_home, name='user_home'),
    path('user-login', views.user_login, name='user_login'),
    path('user-profile', views.user_profile, name='user_profile'),
    path('user-register', views.user_register, name='user_register'),
    path('rapido', views.rapido, name='rapido'),
    path('portor', views.portor, name='portor'),
    path('swiggy-genie', views.Swiggy_genie, name='swiggy_genie'),
    path('Lynk', views.lynk, name='Lynk'),
    path('edit', views.edit, name='edit'),
    path('user-feedback/<int:id>/<str:obj>', views.user_feedback, name='user_feedback')
    
    
    
    
]