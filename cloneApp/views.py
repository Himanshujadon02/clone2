from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path,include
from .forms import Registration
from .models import *

# Create your views here.
# def home_page(request):
#     popularBlogs = Popular_blogs.objects.all()
#     context = {'popularBLOGS':popularBlogs,'name':'Mr.Himanshu',
#     }
#     return render(request,'cloneApp/home.html',context)  



def home_page(request):
    popularBlogs = Popular_blogs.objects.all()
    Why_Netcore = Why_netcore.objects.all()
    About_Us = About.objects.all()
    Our_Involvement = Our_involvement.objects.all()
    TestonoMIAL = Testonomial.objects.all()
    LogO = Logo.objects.all()
    # lanDING=Landing.objects.all()
    context = {'popularBLOGS':popularBlogs,'WhyNETCORE':Why_Netcore,
    'ABOUT':About_Us,
    'OUR':Our_Involvement,
    'TESTONOMIAL':TestonoMIAL,
    'LOGO':LogO,
    # 'LANDING':lanDING,
    'name':'Mr.Himanshu',
    }
    return render(request,'cloneApp/home.html',context)  


def contact(request):
    if request.method == 'POST':
        fm = Registration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            nm = fm.cleaned_data['number']
            mes = fm.cleaned_data['message']

            reg = User(name=nm, email=em, number=nm, message=mes)
            reg.save()
            fm = Registration()
    else:
        fm = Registration()
            
    stu = User.objects.all()
    return render(request,'cloneApp/contactus.html',{'form':fm, 'stu':stu})  