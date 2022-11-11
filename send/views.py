from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def index(request):
    return render(request,"index.html")


def login(request):
    return render(request,"login.html")


def register(request):
    if request.method == "POST":
        username= request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
           if User.objects.filter(username=username).first():
               messages.success(request,"le nom d'utilisateur existe deja")
               return redirect('/register')
           if User.objects.filter(email=email).first():
               messages.success(request,"le mail existe deja")
               return redirect('/register')
           user_obj = User(username=username,email=email)
           user_obj.set_password(password)
           user_obj.save()
           auth_token = str(uuid.uuid4())
           profile_obj = Profile.objects.create(user=user_obj,auth_token=auth_token)
           profile_obj.save()
           send_mail_after_verify(email,auth_token)
           return  render(request,"token_send.html")
        except Exception as e:
            print(e)

    return render(request,"register.html")


def succes(request):
    return render(request,"succes.html")


def token_send(request):
    return render(request,"token_send.html")

def send_mail_after_verify(email,token):
    subject = "Your count need to be verify"
    message =f'Hi paste le link to verify your acount http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,message,email_from,recipient_list)


