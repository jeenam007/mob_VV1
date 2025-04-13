from django.shortcuts import render,redirect
from .models import Cart

def login_required(func):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect('customerapp:userlogin')
        else:
            return func(request,*args,**kwargs)
    return wrapper



