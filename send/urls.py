from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("token_send",views.token_send,name="token_send"),
    path("succes",views.succes,name="succes"),
]