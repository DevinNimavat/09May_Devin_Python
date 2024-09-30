import random
from django.contrib.auth import logout, authenticate,login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.utils.html import escape
from insurance import settings
from .forms import registerform, healthform, lifeform, vehicleform, homeform, travelform, businessform,passform
from .models import insurance


# Create your views here.

def index(request):
    msg=''
    if request.method == 'POST':
        username=request.POST['unm']
        password=request.POST['pas']
        user=insurance.objects.filter(unm=username, pas=password)
        if user.exists():
            print('login success')
            msg = 'Login Successful'
            request.session['user']=username
            return redirect('apply')
        else:
            print('login failed')
            msg = 'Login Failed'
    return render(request, 'index.html', {'msg': msg})


def register(request):
    msg = ''
    if request.method == 'POST':
        new = registerform(request.POST)
        if new.is_valid():
            username = new.cleaned_data.get('unm')
            ex = insurance.objects.filter(unm=username)
            if ex.exists():
                msg = 'User already exists'
            else:
                # Send OTP
                global otp
                otp = random.randint(10000, 99999)
                fnm = request.POST.get('fnm')
                sub = 'Insurance Policy'
                msg = f'Welcome to Insurance Policy Mr/Miss: {fnm}.\n\n Thank You For Registration.\n\n Your OTP is: {otp}.\n\n Thank You'
                from_id = settings.EMAIL_HOST_USER
                to = [request.POST['em']]
                send_mail(subject=sub, message=msg, from_email=from_id, recipient_list=to)

                new.save()
                print('saved')
                msg = 'User created successfully'

                return redirect('otpverify')
        else:
            print(new.errors)
            msg = 'User creation failed'
    return render(request, 'register.html', {'msg': msg})


def otpverify(request):
    msg=''
    global otp
    print(otp)
    if request.method == 'POST':
        if request.POST['sendotp'] == str(otp):
            print('Correct OTP')
            msg = 'OTP Matched'
            return redirect('/')
        else:
            print('Wrong OTP')
            msg = 'OTP Mismatched'
    return render(request, 'otpverify.html', {'msg': msg})


# @login_required(login_url='/')
def apply(request):
    user=request.session.get('user')
    return render(request, 'apply.html',{'user':user})

def health(request):
    msg=''
    global no
    no=random.randint(10000000, 99999999)
    if request.method == 'POST':
        new=healthform(request.POST,request.FILES)
        if new.is_valid():

            # Email
            tp=request.POST['type']
            fnm=request.POST['fullnm']
            sub='Health Insurance Policy'
            mag=f'Hello Mr/Miss {fnm}.\n\n Your Health Insurance Appllid Successfully.\n\nYour Health Policy Number is: {no}.\n\nYour Health Insurance Type is: {tp}.\n\nThank You..'
            from_id=settings.EMAIL_HOST_USER
            to=[request.POST['em']]
            send_mail(subject=sub, message=mag, from_email=from_id, recipient_list=to)
            new.save()
            print('saved')
            msg = 'Health Apply Successfull'

            return redirect('apply')
        else:
            print(new.errors)
            msg = 'Health Apply Failed'

    return render(request, 'health.html',{'msg':msg, 'no':no})

def life(request):
    mag=''
    no=random.randint(10000000,99999999)
    if request.method=='POST':
        new=lifeform(request.POST,request.FILES)
        if new.is_valid():

            # Email
            tp=request.POST['type']
            fnm=request.POST['fullnm']
            sub='Life Insurance Policy'
            msg=f'Hello Mr/Miss {fnm}.\n\n Your Life Insurance Appllid Successfully.Your Life Policy Number is: {no}.Your Life Insurance Type is: {tp}.\n\nThank You..'
            from_id=settings.EMAIL_HOST_USER
            to=[request.POST['em']]
            send_mail(subject=sub, message=msg, from_email=from_id, recipient_list=to)
            new.save()
            print('Life Insurance Apply')
            mag='Life Apply Successfull'
            return redirect('apply')
        else:
            print(new.errors)
            mag='Life Appy Failed'
    return render(request,'life.html',{'mag':mag,'no':no})

def vehicle(request):
    mag=''
    no=random.randint(10000000,99999999)
    if request.method=='POST':
        new=vehicleform(request.POST,request.FILES)
        if new.is_valid():

            # Email
            tp=request.POST['type']
            fnm=request.POST['fullnm']
            sub='Vehicle Insurance Policy'
            msg=f'Hello Mr/Miss {fnm}.\n\n Your Vehicle Insurance Appllid Successfully.Your Vehicle Policy Number is: {no}.Your Vehicle Insurance Type is: {tp}.\n\nThank You..'
            from_id=settings.EMAIL_HOST_USER
            to=[request.POST['em']]
            send_mail(subject=sub, message=msg, from_email=from_id, recipient_list=to)
            new.save()
            print('Vehicle Insurance Apply')
            mag='Vehicle Apply Successfully'
            return redirect('apply')
        else:
            print(new.errors)
            mag='Vehicle Apply Failed'
    return render(request, 'vehicle.html',{'msg':mag, 'no':no})

def userlogout(request):
    logout(request)
    return redirect('/')

def home(request):
    msg=''
    no=random.randint(10000000, 99999999)
    if request.method == 'POST':
        new=homeform(request.POST,request.FILES)
        if new.is_valid():

            # Email
            tp=request.POST['type']
            fnm=request.POST['fullnm']
            sub='Home Insurance Policy'
            msg=f'Hello Mr/Miss {fnm}.\n\n Your Home Insurance Appllid Successfully.Your Home Policy Number is: {no}.Your Home Insurance Type is: {tp}.\n\nThank You..'
            from_id=settings.EMAIL_HOST_USER
            to=[request.POST['em']]
            send_mail(subject=sub, message=msg, from_email=from_id, recipient_list=to)
            new.save()
            print('saved')
            msg = 'Home Insurance Apply Successfull'
            return redirect('apply')
        else:
            print(new.errors)
            msg = 'Home Insurance Apply Failed'
    return render(request, 'home.html',{'msg':msg, 'no':no})

def travel(request):
    msg=''
    no=random.randint(10000000, 99999999)
    if request.method == 'POST':
        new=travelform(request.POST,request.FILES)
        if new.is_valid():

            # Email
            tp=request.POST['type']
            fnm=request.POST['fullnm']
            sub='Travel Insurance Policy'
            msg=f'Hello Mr/Miss {tp}.\n\n Your Travel Insurance Appllid Successfully.Your Travel Policy Number is: {no}.Your Travel Insurance Type is: {tp}.\n\nThank You..'
            from_id=settings.EMAIL_HOST_USER
            to=[request.POST['em']]
            send_mail(subject=sub, message=msg, from_email=from_id, recipient_list=to)

            new.save()
            print('saved')
            msg = 'Travel Insurance Apply Successfull'
            return redirect('apply')
        else:
            print(new.errors)
            msg = 'Travel Insurance Apply Failed'
    return render(request,'travel.html',{'msg':msg, 'no':no})

def business(request):
    mag=''
    no=random.randint(10000000, 99999999)
    if request.method=='POST':
        new=businessform(request.POST,request.FILES)
        if new.is_valid():

            # Email
            tp=request.POST['type']
            fnm=request.POST['fullnm']
            sub='Business Insurance Policy'
            mag=f'Hello Mr/Miss {fnm}.\n\n Your Business Insurance Appllid Successfully.Your Business Policy Number is: {no}.Your Business Insurance Type is: {tp}.\n\nThank You..'
            from_id=settings.EMAIL_HOST_USER
            to=[request.POST['business_em']]
            send_mail(subject=sub, message=mag, from_email=from_id, recipient_list=to)

            new.save()
            print('Business Insurance Apply')
            mag='Business Apply Successfully'
            return redirect('apply')
        else:
            print(new.errors)
            mag='Business Apply Failed'
    return render(request, 'business.html',{'mag':mag, 'no':no})

def email_verify(request):

    if request.method == 'POST':
        email=request.POST['em']
        umail=insurance.objects.get(em=email)
        request.session['uid']=umail.id
        print('Email Verified')
        return redirect('reset_password')
    else:
        print('error')
    return render(request, 'email_verify.html',)

def reset_password(request):

    if request.method == 'POST':
        newpas=passform(request.POST)
        new=request.session.get('uid')
        uid=insurance.objects.get(id=new)
        if newpas.is_valid():
            newpass=passform(request.POST,instance=uid)
            newpass.save()
            print('Password Changed')
            return redirect('/')
        else:
            print(newpas.errors)
    return render(request, 'reset_password.html',)