from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404,reverse
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.conf import settings
from django.template import loader
# Create your views here.
from django.shortcuts import render

from mainapp import views
from django.core.mail import EmailMessage
from .models import Partner_Register
from .models import *
from captainapp.models import Captain_Register
from userapp.models import *

def partner_registration (request):
    if request.method == "POST" and request.FILES["image"] and request.FILES["Licences"] :
        name = request.POST['name']
        city = request.POST['city']
        lic_num = request.POST['lic_num']
        partner = request.POST['partener']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['pass']
        image = request.FILES['image']
        Licences = request.FILES['Licences']
        try:
            if len(name) > 20:
                messages.error (request, "user name must be 10 characters")
            
            elif  Partner_Register.objects.filter(par_email=email).exists():
                messages.error (request, "Email alredy exist")
            elif  Partner_Register.objects.filter(par_phone=phone).exists():
                messages.error (request, "Phone Number alredy exist")
        except:
            reg_details = Partner_Register.objects.create(partner=partner,par_name=name,par_phone=phone,par_license=lic_num,city=city,par_email=email,par_pwd=password,par_image=image,par_lic=Licences)
            reg_details.save()
            return redirect('partner_login')

    return render (request, './partner/partner-registration.html')

def partner_login (request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pass')
        try:
            login = Partner_Register.objects.get(par_email=email,par_pwd=password)
            request.session["p_email"]=login.par_email
            request.session["demo"]=login.partner
            status = login.status
            if status == "Accepted":
                return redirect ("partner_home")
                
            else : 
                messages.success(request, "your account not at activated")
        except:
            messages.error(request, "bad credential Please Register")
            return redirect("partner_login")
    return render (request, './partner/partner-login.html')


def partner_home (request):
    return render (request, './partner/partner-home.html')

def partner_profile (request):
   
    obj = Partner_Register.objects.get(par_email=request.session["p_email"])

    
    context = {
        'obj' : obj
    }
    
    return render (request, './partner/partner-profile.html', context=context)


def partner_feedback (request):
    login = Partner_Register.objects.get(par_email=request.session["p_email"])
    demo = login.partner
    
    if demo == "Rapido":
        print("1")
        obj = User_feedback.objects.filter(orgniztion="Rapido")
    elif demo == "Swiggy_Genie":
        print("2")
        obj = User_feedback.objects.filter(orgniztion="Swiggy_Genie")
    elif demo == "Porter" :
        print("3")
        obj = User_feedback.objects.filter(orgniztion="Porter")
    elif demo == 'Lynk':
        print("4")
        obj = User_feedback.objects.filter(orgniztion="Lynk")
    


    return render (request, './partner/feedback.html', {'view':obj})


def acc_rej (request):
    login = Partner_Register.objects.get(par_email=request.session["p_email"])
    demo = login.partner
    
    if demo == "Rapido":
        print("1")
        obj = Captain_Register.objects.filter(vechicle='Rapido')
    elif demo == "Swiggy_Genie":
        print("2")
        obj = Captain_Register.objects.filter(vechicle='Swiggy_Genie')
    elif demo == "Porter" :
        print("3")
        obj = Captain_Register.objects.filter(vechicle='Porter')
    elif demo == 'Lynk':
        print("4")
        obj = Captain_Register.objects.filter(vechicle='Lynk')

     
    
    return render (request, './partner/acc-rej.html', {'view':obj})


def add_details (request):
    obj = Two_wheeler.objects.filter(name=request.session["demo"])
    print(request.session["demo"])
    if request.session["demo"] == "Porter":
        demo = Four_wheeler.objects.all()
        context={
            "view":demo
        }
    elif request.session["demo"] == "Lynk":
        demo = Lynk_Four_wheeler.objects.all()
        context={
            "view" : demo
        }
    else :
        obj = Two_wheeler.objects.filter(name=request.session["demo"])
        context = {
            "view" : obj
        }
    
   

    return render (request, './partner/add-details.html', context=context)


def edit_details (request, id):
    obj = Two_wheeler.objects.filter(name=request.session["demo"])
    print(request.session["demo"])
    if request.session["demo"] == "Porter":
        obj = Four_wheeler.objects.get(assign_id=id)
        context = {
            'obj' : obj
        }
        if request.method == "POST" :
            name = request.POST.get('name')
            price = request.POST.get('price')
            
            
            data = get_object_or_404(Four_wheeler, assign_id=id)
            data.name = name
            data.price = price
            data.save(update_fields=["name","price"])
            data.save()
            return redirect("add_details")
    else:
        obj = Two_wheeler.objects.get(assign_id=id)
        context = {
            'obj' : obj
        }
        if request.method == "POST" :
            name = request.POST.get('name')
            price = request.POST.get('price')
            
            
            data = get_object_or_404(Two_wheeler, assign_id=id)
            data.name = name
            data.price = price
            data.save(update_fields=["name","price"])
            data.save()
            return redirect("add_details")
    
    return render (request, './partner/edit-details.html', context=context)


def accept_cap(request, id) : 
    accept = get_object_or_404(Captain_Register, assign_id=id)
    accept.status = 'Accepted'
    accept.save(update_fields = ['status'])
    accept.save()
    ac = accept.cap_email
    acc = accept.cap_pwd
    email = EmailMessage('Subject',f'Hello {ac}, your account is activated\nhere your details\n username : {ac} \n Password : {acc}', to=[ ac ])
    email.send()
    return redirect("acc_rej")

def reject_cap(request, id) : 
    reject = get_object_or_404(Captain_Register, assign_id=id)
    reject.status = 'Rejected'
    reject.save(update_fields = ['status'])
    reject.save()
    re = reject.cap_email
    
    email = EmailMessage('Subject',f'Hello {re}, your account is rejected pls rejecter again', to=[ re ])
    email.send()
    return redirect("acc_rej")

def delecap(request, id):
    flights = Captain_Register.objects.get(assign_id=id)
    flights.delete()
    return redirect('acc_rej')
