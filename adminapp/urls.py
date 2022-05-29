from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views 
urlpatterns = [
    
    path('admin-dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('admin-login', views.admin_login, name='admin_login'),
    path('admin-view-booking', views.admin_view_booking, name='admin_view_booking'),
    path('admin-view-partners', views.admin_view_partners, name='admin_view_partners'),
    path('admin-view-feedback', views.admin_view_feedback, name='admin_view_feedback'),
    path('admin-view-captains', views.admin_view_captains, name='admin_view_captains'),
    path('demo', views.demo, name='demo'),
    path('accept_par/<int:id>', views.accept_par, name='accept_par'),
    path('reject_par/<int:id>', views.reject_par, name='reject_par')

    
    
]