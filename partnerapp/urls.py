from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
     path('partner-registration', views.partner_registration, name='partner_registration'),
     path('partner-login', views.partner_login, name='partner_login'),
     path('partner-home', views.partner_home, name='partner_home'),
     path('partner-profile', views.partner_profile, name='partner_profile'),
     path('partner-feedback', views.partner_feedback, name='partner_feedback'),
     path('add-details', views.add_details, name='add_details'),
     path('edit_details/<int:id>', views.edit_details, name='edit_details'),
     path('acc-rej', views.acc_rej, name='acc_rej'),
     path('accept_cap/<int:id>', views.accept_cap, name='accept_cap'),
     path('reject_cap/<int:id>', views.reject_cap, name='reject_cap'),
     path('delecap/<int:id>', views.delecap, name='delecap')

]