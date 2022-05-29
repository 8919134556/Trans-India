from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404,reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.template import loader
# Create your views here.
from django.shortcuts import render
import requests
from mainapp import views
from . import views
from django.core.mail import EmailMessage

from .models import Captain_Register
from userapp.models import *
from .models import *

def captain_register (request):
	if request.method == "POST" and request.FILES["file"] and request.FILES["Licences"] and request.FILES["cap_vehicle"]:
		
		name = request.POST['fname']
		phone = request.POST['phone']
		lic_num = request.POST['lic_num']
		city = request.POST['city']
		vehicle = request.POST['vehicle']
		email = request.POST['email']
		password = request.POST['pass']
		image = request.FILES['file']
		cap_vehicle_image = request.FILES['cap_vehicle']
		cap_driving_lic = request.FILES['Licences']
		try:
			if len(name) > 20:
				messages.error (request, "user name must be 10 characters")
			
			elif  Captain_Register.objects.filter(cap_email=email).exists():
				messages.error (request, "Email alredy exist")
			elif  Captain_Register.objects.filter(cap_phone=phone).exists():
				messages.error (request, "Phone Number alredy exist")
				


		except:
			reg_details = Captain_Register.objects.create(cap_name=name,cap_phone=phone,cap_license=lic_num,city=city,vechicle=vehicle,cap_email=email,cap_pwd=password,cap_image=image,cap_vehicle_image=cap_vehicle_image,cap_driving_lic=cap_driving_lic)
			reg_details.save()
			return redirect('captain_login')
	   
	return render (request, './captain/captain-register.html')
    
    
	
def captain_login (request):
	if request.method == "POST":
		email = request.POST.get('email')
		password = request.POST.get('pass')
		try:
			login = Captain_Register.objects.get(cap_email=email,cap_pwd=password)
			request.session["cap_email"]=login.cap_email
			request.session["cap_phone"]=login.cap_phone
			status = login.status
			if status == "Accepted" :
				messages.success(request, "welcome")
				return redirect ("captain_home")
			else :
				messages.error(request, "your account not at activated")
                
			
  
		except:
			messages.error(request, "bad credential Please Register")
			return redirect("captain_login")
        	
	return render (request, './captain/captain-login.html')


    

def captain_feedback (request):
	obj = User_feedback.objects.filter(phone=request.session["cap_phone"])
	return render (request, './captain/captain-feedback.html', {'view' : obj})
    
def captain_home (request):
    return render (request, './captain/captain-home.html')

def captain_order1 (request):
	login = Captain_Register.objects.get(cap_email=request.session["cap_email"])
	demo = login.vechicle
    
	if demo == "Rapido":
		print("1")
		obj1 = Captain_Register.objects.get(cap_email=request.session["cap_email"])
		demo = obj1.cap_phone
		obj = Rapido.objects.filter(cap_name=demo)

		
	elif demo == "Swiggy_Genie":
		print("2")
		obj1 = Captain_Register.objects.get(cap_email=request.session["cap_email"])
		demo = obj1.cap_phone
		obj = swiggy_genie.objects.filter(cap_name=demo)

		
		
	elif demo == "Porter" :
		print("3")
		obj1 = Captain_Register.objects.get(cap_email=request.session["cap_email"])
		demo = obj1.cap_phone
		obj = Portor.objects.filter(cap_name=demo)

		
		
	elif demo == 'Lynk':
		print("4")
		obj1 = Captain_Register.objects.get(cap_email=request.session["cap_email"])
		demo = obj1.cap_phone
		obj = Lynk.objects.filter(cap_name=demo)

		
	return render (request, './captain/captain-order.html', {'view':obj})

def captain_order (request, id):
	login = Captain_Register.objects.get(cap_email=request.session["cap_email"])
	demo = login.vechicle
    
	if demo == "Rapido":
		print("1")
		obj1 = Captain_Register.objects.get(cap_email=request.session["cap_email"])
		demo = obj1.cap_phone
		obj = Rapido.objects.filter(cap_name=demo)

		accept = get_object_or_404(Rapido, a_id=id)
		accept.status = 'Complete'
		accept.save(update_fields = ['status'])
		accept.save()
		
	elif demo == "Swiggy_Genie":
		print("2")
		obj1 = Captain_Register.objects.get(cap_email=request.session["cap_email"])
		demo = obj1.cap_phone
		obj = swiggy_genie.objects.filter(cap_name=demo)

		accept = get_object_or_404(swiggy_genie, a_id=id)
		accept.status = 'Complete'
		accept.save(update_fields = ['status'])
		accept.save()
		
	elif demo == "Porter" :
		print("3")
		obj1 = Captain_Register.objects.get(cap_email=request.session["cap_email"])
		demo = obj1.cap_phone
		obj = Portor.objects.filter(cap_name=demo)

		accept = get_object_or_404(Portor, a_id=id)
		accept.status = 'Complete'
		accept.save(update_fields = ['status'])
		accept.save()
		
	elif demo == 'Lynk':
		print("4")
		obj1 = Captain_Register.objects.get(cap_email=request.session["cap_email"])
		demo = obj1.cap_phone
		obj = Lynk.objects.filter(cap_name=demo)

		accept = get_object_or_404(Lynk, a_id=id)
		accept.status = 'Complete'
		accept.save(update_fields = ['status'])
		accept.save()
		
		

	return render (request, './captain/captain-order.html', {'view':obj})



def captain_profile (request):
	login = Captain_Register.objects.get(cap_email=request.session["cap_email"])
	context = {
		'obj' : login
	}
	if request.method == "POST" :
		name = request.POST.get('new-pass')
		data = get_object_or_404(Captain_Register, cap_email=request.session["cap_email"])
		data.cap_pwd = name
		data.save(update_fields=["cap_pwd"])
		data.save()
		return redirect("captain_profile")
	return render (request, './captain/captain-profile.html', context=context)


def base (request):
    return render (request, './captain/base.html')

def order (request):
	login = Captain_Register.objects.get(cap_email=request.session["cap_email"])
	demo = login.vechicle
    
	if demo == "Rapido":
		print("1")
		obj = Rapido.objects.all()
		obj1 = Captain_Register.objects.get(cap_email=request.session["cap_email"])
	elif demo == "Swiggy_Genie":
		print("2")
		obj = swiggy_genie.objects.all()
		obj1 = Captain_Register.objects.get(cap_email=request.session["cap_email"])
	elif demo == "Porter" :
		print("3")
		obj = Portor.objects.all()
		obj1 = Captain_Register.objects.get(cap_email=request.session["cap_email"])
	elif demo == 'Lynk':
		print("4")
		obj = Lynk.objects.all()
		obj1 = Captain_Register.objects.get(cap_email=request.session["cap_email"])
	
	
	
	
	

	return render (request, './captain/orders.html', {'view':obj, 'ob':obj1})


def route(request):

	context = {"google_api_key": settings.GOOGLE_API_KEY}
	return render(request, './captain/route.html', context)

def ride(request, id, email, c_na,c_id):
	login = Captain_Register.objects.get(cap_email=request.session["cap_email"])
	demo = login.vechicle
    
	if demo == "Rapido":
		print("1")
		obj = Rapido.objects.get(a_id=id)
		obj1 = User_Register.objects.get(user_email=email)
		var = obj1.user_phone
		
		accept = get_object_or_404(Rapido, a_id=id)
		accept.status = 'Accepted'
		accept.cap_id = c_id
		accept.cap_name = c_na
		accept.save(update_fields = ['status', 'cap_id', 'cap_name'])
		accept.save()
		url = "https://www.fast2sms.com/dev/bulkV2"
		my_data = {
			'sender_id': 'FSTSMS',
			'message': f'Welcome to Trans India, \n Here Your Captain Details\n Captain Name : {c_id}  \n Captain Phone No : {c_na}',
			'language': 'english',
			'route': 'p',     
			'numbers': var          

		}
		headers = {
			'authorization': 'Eo9rPn2wdSa5Bl47z1bZRfypFLXvtWmIAi0cJGHe3qDjVsg8QM56IZGlyDb2soaSQdWFXme8AnVj0v47',
			'Content-Type': "application/x-www-form-urlencoded",
			'Cache-Control': "no-cache"
		}
		response = requests.request("POST",
									url,
									data = my_data,
									headers = headers)
		if request.method == "POST" :
			data = request.POST['otp']
			obj1.user_otp == data
			data2 = "complete"
	elif demo == "Swiggy_Genie":
		print("2")
		obj = swiggy_genie.objects.get(a_id=id)
		obj1 = User_Register.objects.get(user_email=email)
		var = obj1.user_phone
		print(var)
		accept = get_object_or_404(swiggy_genie, a_id=id)
		accept.status = 'Accepted'
		accept.cap_id = c_id 
		accept.cap_name = c_na
		accept.save(update_fields = ['status', 'cap_id', 'cap_name'])
		accept.save()
		url = "https://www.fast2sms.com/dev/bulkV2"
		my_data = {
			'sender_id': 'FSTSMS',
			'message': f'Welcome to Trans India, \n Here Your Captain Details \n Captain Name : {c_id}  \n Captain Phone No : {c_na}',
			'language': 'english',
			'route': 'p',     
			'numbers': var          

		}
		headers = {
			'authorization': 'Eo9rPn2wdSa5Bl47z1bZRfypFLXvtWmIAi0cJGHe3qDjVsg8QM56IZGlyDb2soaSQdWFXme8AnVj0v47',
			'Content-Type': "application/x-www-form-urlencoded",
			'Cache-Control': "no-cache"
		}
		response = requests.request("POST",
									url,
									data = my_data,
									headers = headers)
	elif demo == "Porter" :
		print("3")
		obj = Portor.objects.get(a_id=id)
		obj1 = User_Register.objects.get(user_email=email)
		var = obj1.user_phone
		print(var)
		accept = get_object_or_404(Portor, a_id=id)
		accept.status = 'Accepted'
		accept.cap_id = c_id 
		accept.cap_name = c_na
		accept.save(update_fields = ['status', 'cap_id', 'cap_name'])
		accept.save()
		url = "https://www.fast2sms.com/dev/bulkV2"
		my_data = {
			'sender_id': 'FSTSMS',
			'message': f'Welcome to Trans India, \n Here Your Captain Details \n Captain Name : {c_id}  \n Captain Phone No : {c_na}',
			'language': 'english',
			'route': 'p',     
			'numbers': var          

		}
		headers = {
			'authorization': 'Eo9rPn2wdSa5Bl47z1bZRfypFLXvtWmIAi0cJGHe3qDjVsg8QM56IZGlyDb2soaSQdWFXme8AnVj0v47',
			'Content-Type': "application/x-www-form-urlencoded",
			'Cache-Control': "no-cache"
		}
		response = requests.request("POST",
									url,
									data = my_data,
									headers = headers)
	elif demo == 'Lynk':
		print("4")
		obj = Lynk.objects.get(a_id=id)
		obj1 = User_Register.objects.get(user_email=email)
		var = obj1.user_phone
		print(var)
		accept = get_object_or_404(Lynk, a_id=id)
		accept.status = 'Accepted'
		accept.cap_id = c_id
		accept.cap_name = c_na
		accept.save(update_fields = ['status', 'cap_id', 'cap_name'])
		accept.save()
		url = "https://www.fast2sms.com/dev/bulkV2"
		my_data = {
			'sender_id': 'FSTSMS',
			'message': f'Welcome to Trans India, \n Here Your Captain Details \n Captain Name : {c_id}  \n Captain Phone No : {c_na}',
			'language': 'english',
			'route': 'p',     
			'numbers': var          

		}
		headers = {
			'authorization': 'Eo9rPn2wdSa5Bl47z1bZRfypFLXvtWmIAi0cJGHe3qDjVsg8QM56IZGlyDb2soaSQdWFXme8AnVj0v47',
			'Content-Type': "application/x-www-form-urlencoded",
			'Cache-Control': "no-cache"
		}
		response = requests.request("POST",
									url,
									data = my_data,
									headers = headers)
	
	
	
	context={
		'obj':obj,
		'obj1':obj1
	}

	return render(request, './captain/ride.html', context=context)

