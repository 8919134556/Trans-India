from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.template import loader
# Create your views here.
from django.shortcuts import render
from mainapp import views
from django.core.mail import EmailMessage
from .models import User_Register
from .models import Rapido
from .models import *
from partnerapp.models import Two_wheeler
from partnerapp.models import Four_wheeler
from partnerapp.models import Lynk_Four_wheeler
from captainapp.models import Captain_Register
import math, random
import requests



def user_booking (request):
    obj = Rapido.objects.filter(user_email=request.session["email"])
    
    obj1 = Portor.objects.filter(user_email=request.session["email"])
    obj2 = swiggy_genie.objects.filter(user_email=request.session["email"])
    obj3 = Lynk.objects.filter(user_email=request.session["email"])
    
    
    
    
   

    return render (request, './user/user-booking.html', {'view':obj, 'view1':obj1, 'view2':obj2, 'view3':obj3})

def user_home (request):
    demo = Four_wheeler.objects.all()
    obj = Two_wheeler.objects.get(name='Rapido')
    obj1 = Two_wheeler.objects.get(name='Porter')
    obj2 = Two_wheeler.objects.get(name='Swiggy_Genie')
    obj3 = Two_wheeler.objects.get(name='Lynk')

    
    context = {
            'obj' : obj,
            'obj1' : obj1,
            'obj2' : obj2,
            'obj3' : obj3,
            'demo':demo
        }

    return render (request, './user/user-home.html', context=context)

def user_login (request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            login = User_Register.objects.get(user_email=email,user_pwd=password)
            request.session["email"]=login.user_email
            return redirect ("user_home")
        except:
            messages.error(request, "bad credential Please Register")
            return redirect("user_login")
    return render (request, './user/user-login.html')

def user_profile (request):
    login = User_Register.objects.get(user_email=request.session["email"])
    context = {
        'obj':login
    }
    return render (request, './user/user-profile.html', context=context)

def user_register (request):
    if request.method == "POST" and request.FILES["image"] :
        name = request.POST['fname']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        image = request.FILES['image']
        try:
            if len(name) > 20:
                messages.error (request, "user name must be 10 characters")
            
            elif  User_Register.objects.filter(user_email=email).exists():
                messages.error (request, "Email alredy exist")
            elif  User_Register.objects.filter(user_phone=phone).exists():
                messages.error (request, "Phone Number alredy exist")
        except:
            digits = "0123456789"
            OTP = ""
    
            # length of password can be changed
            # by changing value in range
            for i in range(4) :
                OTP += digits[math.floor(random.random() * 10)]

            reg_details = User_Register.objects.create(user_name=name,user_phone=phone,user_email=email,user_pwd=password,user_image=image, user_otp=OTP)
            reg_details.save()
            email = EmailMessage('Subject',f'Hello {name},\nwe glad to inform you \nHere Your Details:\nYour OTP no : {OTP}\nUsername : {email}\nPassword : {password}', to=[ email ])
            email.send()
            url = "https://www.fast2sms.com/dev/bulkV2"
            my_data = {
                'sender_id': 'FSTSMS',
                'message': f'Welcome to Trans India, \n Here Your OTP : {OTP}  \n Note: Do not Share your OTP',
                'language': 'english',
                'route': 'p',     
                'numbers': phone          

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


            return redirect('user_login')

    return render (request, './user/user-register.html')

def rapido(request):
    demo = Four_wheeler.objects.all()
    obj = Two_wheeler.objects.get(name='Rapido')
    
    context = {
            'obj' : obj,
            'demo' : demo
        }
    
    
    if request.method == "POST" :
        orgine = request.POST.get('starting')
        destination = request.POST.get('ending')
        distance = request.POST.get('distance')
        subtotal = request.POST.get('subtotal')
        gst = request.POST.get('gst')
        total = request.POST.get('total')
        reg_details = Rapido.objects.create(orgine=orgine,destination=destination,distance=distance,subtotal=subtotal,gst=gst,total=total, user_email=request.session["email"])
        reg_details.save()
        return redirect('user_booking')
        
        

    return render (request, './user/rapido.html',context=context)

def portor(request):
    obj = Four_wheeler.objects.get(name="Tata_Ace")
    obj1 = Four_wheeler.objects.get(name="Ashok_Leyland_Dost")
    obj2 = Four_wheeler.objects.get(name="Eicher_Carrier")
    obj3 = Four_wheeler.objects.get(name="Piaggio")
    obj4 = Four_wheeler.objects.get(name="Super_Ace_8ft")
    
    
    context = {
            'obj' : obj,
            'obj1': obj1,
            'obj2' : obj2,
            'obj3':obj3,
            'obj4':obj4
        }
    
    
    if request.method == "POST" :
        orgine = request.POST.get('starting')
        destination = request.POST.get('ending')
        distance = request.POST.get('distance')
        subtotal = request.POST.get('subtotal')
        vehicle = request.POST.get('vehicle')
        gst = request.POST.get('gst')
        total = request.POST.get('total')
        reg_details = Portor.objects.create(orgine=orgine,destination=destination,distance=distance,subtotal=subtotal,gst=gst,total=total, user_email=request.session["email"], vechile_type=vehicle)
        reg_details.save()
        return redirect('user_booking')
        
        

    return render (request, './user/portor.html',context=context)

def Swiggy_genie(request):
    obj = Two_wheeler.objects.get(name='Swiggy_Genie')
    
    context = {
            'obj' : obj
        }
    
    
    if request.method == "POST" :
        orgine = request.POST.get('starting')
        destination = request.POST.get('ending')
        distance = request.POST.get('distance')
        subtotal = request.POST.get('subtotal')
        gst = request.POST.get('gst')
        total = request.POST.get('total')
        reg_details = swiggy_genie.objects.create(orgine=orgine,destination=destination,distance=distance,subtotal=subtotal,gst=gst,total=total, user_email=request.session["email"])
        reg_details.save()
        return redirect('user_booking')
        
        

    return render (request, './user/swiggy-genie.html',context=context)

def lynk(request):
    obj = Lynk_Four_wheeler.objects.get(name="Tata_Ace")
    obj1 = Lynk_Four_wheeler.objects.get(name="Ashok_Leyland_Dost")
    obj2 = Lynk_Four_wheeler.objects.get(name="Eicher_Carrier")
    obj3 = Lynk_Four_wheeler.objects.get(name="Piaggio")
    obj4 = Lynk_Four_wheeler.objects.get(name="Super_Ace_8ft")
    
    
    context = {
            'obj' : obj,
            'obj1': obj1,
            'obj2' : obj2,
            'obj3':obj3,
            'obj4':obj4
        }
    
    
    if request.method == "POST" :
        orgine = request.POST.get('starting')
        destination = request.POST.get('ending')
        distance = request.POST.get('distance')
        subtotal = request.POST.get('subtotal')
        gst = request.POST.get('gst')
        vehicle = request.POST.get('vehicle')
        total = request.POST.get('total')
        reg_details = Lynk.objects.create(orgine=orgine,destination=destination,distance=distance,subtotal=subtotal,gst=gst,total=total, user_email=request.session["email"], vechile_type=vehicle)
        reg_details.save()
        return redirect('user_booking')
        
        

    return render (request, './user/Lynk.html',context=context)

def edit (request):
    login = User_Register.objects.get(user_email=request.session["email"])
    context = {
        'obj':login
    }
    return render (request, "./user/user-edit.html", context=context)
 
def user_feedback(request, id, obj):
    
    if obj == "Rapido":
        print("1")
        demo = Rapido.objects.get(a_id=id)
           
        obj4 = User_feedback.objects.filter(orgniztion=obj, order_id=id)   
        if obj4.exists():
            messages.error(request, "already you provide feedback")
            return redirect("user_booking")
            
        else:
            if request.method == "POST":
                
                name = request.POST['name']
                phone = request.POST['phone']
                orgniztion = request.POST['orgniztion']
                description = request.POST['description']
                
                star = request.POST['stars']
                
                feedback = User_feedback.objects.create(name=name,phone=phone,orgniztion=orgniztion,order_id=id,description=description, rating=star)
                feedback.save()
                return redirect("user_booking")
            

        
    elif obj == "swiggy_genie":
        print("2")
        
        demo = swiggy_genie.objects.get(a_id=id)
        
        obj4 = User_feedback.objects.filter(orgniztion=obj, order_id=id)   
        if obj4.exists():
            messages.error(request, "already you provide feedback")
            return redirect("user_booking")
            
        else:
            if request.method == "POST":
                
                name = request.POST['name']
                phone = request.POST['phone']
                orgniztion = request.POST['orgniztion']
                description = request.POST['description']
                
                star = request.POST['stars']
                
                feedback = User_feedback.objects.create(name=name,phone=phone,orgniztion=orgniztion,order_id=id,description=description, rating=star)
                feedback.save()
                return redirect("user_booking")

        
        
    elif obj == "Porter" :
        print("3")
        demo = Portor.objects.get(a_id=id) 
        obj4 = User_feedback.objects.filter(orgniztion=obj, order_id=id)   
        if obj4.exists():
            messages.error(request, "already you provide feedback")
            return redirect("user_booking")
            
        else:
            if request.method == "POST":
                
                name = request.POST['name']
                phone = request.POST['phone']
                orgniztion = request.POST['orgniztion']
                description = request.POST['description']
                
                star = request.POST['stars']
                
                feedback = User_feedback.objects.create(name=name,phone=phone,orgniztion=orgniztion,order_id=id,description=description, rating=star)
                feedback.save()
                return redirect("user_booking")
            
        
        

        
    elif obj == 'Lynk':
        print("4")
        demo = Lynk.objects.get(a_id=id) 
        obj4 = User_feedback.objects.filter(orgniztion=obj, order_id=id)   
        if obj4.exists():
            messages.error(request, "already you provide feedback")
            return redirect("user_booking")
            
        else:
            if request.method == "POST":
                
                name = request.POST['name']
                phone = request.POST['phone']
                orgniztion = request.POST['orgniztion']
                description = request.POST['description']
                
                star = request.POST['stars']
                
                feedback = User_feedback.objects.create(name=name,phone=phone,orgniztion=orgniztion,order_id=id,description=description, rating=star)
                feedback.save()
                return redirect("user_booking")
        
        

        

    return render (request, "./user/user-feedback.html", {'demo':demo, 'obj':obj})
