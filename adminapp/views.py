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
import requests
from partnerapp.models import Partner_Register
from captainapp.models import Captain_Register
from userapp.models import *

def admin_login (request):
    if request.method == "POST":
        admin_email = request.POST.get('email')
        admin_pws = request.POST.get ('pass')
        if admin_email =='admin' and admin_pws =='admin':
            messages.success(request, "welcome")
            return redirect('admin_dashboard')
            
        else:
            messages.error(request, "bad credential Please Register")
            return redirect('admin_login')
    return render(request, './admin/admin-signin.html')

def admin_dashboard (request):
    obj = User_Register.objects.all().count()
    obj1 = Partner_Register.objects.all().count()
    obj2 = Captain_Register.objects.all().count()
    demo = Rapido.objects.all().count()
    demo1 = Portor.objects.all().count()
    demo2 = swiggy_genie.objects.all().count()
    demo3 = Lynk.objects.all().count()
    demo4 = demo + demo1 + demo2 + demo3

    return render(request, './admin/admin-home.html', {'obj' : obj, 'obj1' : obj1, "obj2" : obj2, 'demo4':demo4})

def admin_view_booking (request) :
    obj = Rapido.objects.all()
    obj1 = Portor.objects.all()
    obj2 = swiggy_genie.objects.all()
    obj3 = Lynk.objects.all()

    return render (request, './admin/admin-view-bookings.html', {'view':obj, 'view1':obj1, 'view2':obj2, 'view3':obj3})

def admin_view_partners (request):
    obj = Partner_Register.objects.all()
    return render(request, './admin/admin-view-partner.html', {'view':obj})

def admin_view_captains (request) :
    obj = Captain_Register.objects.all()
    return render (request, './admin/admin-view-captain.html', {'view':obj})

def admin_view_feedback (request):
    obj = User_feedback.objects.all()
    return render (request, './admin/admin-view-feedbacks.html', {'view':obj})

def demo(request):
    if request.method=="POST":
        mobile = request.POST.get("mobile")      
        # mention url
        url = "https://www.fast2sms.com/dev/bulkV2"
        
        # create a dictionary
        my_data = {
            # Your default Sender ID
            'sender_id': 'FSTSMS',            
            # Put your message here!
            'message': 'click my video https://tiny.one/vamoo',            
            'language': 'english',
            'route': 'p',            
            # You can send sms to multiple numbers
            # separated by comma.
            'numbers':  mobile  
        }
        # create a dictionary
        headers = {
            'authorization': 'fNlrZXEkJUBgiMQLCW9PIzy6VYncqKwdGHF2OA48haRpo3jmTsTAcxw9SLDtE0Pzq8fdC1n2lRGHXkr5',
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache"
        }
        # make a post request
        response = requests.request("POST",
                                    url,
                                    data = my_data,
                                    headers = headers)
        # print the send message
        print(response.text)        
    return render(request,'./admin/demo.html')


def accept_par(request, id) : 
    accept = get_object_or_404(Partner_Register, assign_id=id)
    accept.status = 'Accepted'
    accept.save(update_fields = ['status'])
    accept.save()
    ac = accept.par_email
    acc = accept.par_pwd
    email = EmailMessage('Subject',f'Hello {ac}, your account is activated\nhere your details\n username : {ac} \n Password : {acc}', to=[ ac ])
    email.send()
    return redirect("admin_view_partners")

def reject_par(request, id) : 
    reject = get_object_or_404(Partner_Register, assign_id=id)
    reject.status = 'Rejected'
    reject.save(update_fields = ['status'])
    reject.save()
    re = reject.par_email
    
    email = EmailMessage('Subject',f'Hello {re}, your account is rejected pls rejecter again', to=[ re ])
    email.send()
    return redirect("admin_view_partners")