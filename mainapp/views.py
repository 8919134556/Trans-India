from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import loader
# Create your views here.
from django.shortcuts import render

from django.core.mail import EmailMessage
from partnerapp.models import Two_wheeler

def home(request):
    obj = Two_wheeler.objects.all()
    return render (request, './main/home-index.html', {'view' : obj})