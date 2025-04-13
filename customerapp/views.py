from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm,User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .forms import LoginForm
from mobileapp.decorators import login_required


# Create your views here.

def registration(request):
    
    if request.method =="POST":
       form=UserRegistrationForm(request.POST)
       if form.is_valid():
          form.save()
          messages.success(request, "User registered successfully!")
          return redirect("customerapp:userlist")
       else:
          messages.error(request,"Registration failed.")
    else:
        form=UserRegistrationForm()
    return render(request,'user/registration.html',{'form':form})

def userlist(request):
        userlst=User.objects.all()
        return render(request,'user/userlist.html',{'userlst':userlst})

def useredit(request,id):
     instance_edituser=User.objects.get(id=id)
     if request.POST:
          form=UserRegistrationForm(request.POST,instance=instance_edituser)
          if form.is_valid():
               form.save()
               messages.success(request, "User updated successfully!")
          return redirect('customerapp:userlist')
     else:
          form=UserRegistrationForm(instance=instance_edituser)
          return render(request,'user/registration.html',{'form':form})


     
def userdelete(request,id):
     instance=User.objects.get(id=id)
     instance.delete()
     messages.success(request, "User deleted successfully!")
     return redirect('customerapp:userlist')

def userdet(request,id):
     usrlst=User.objects.get(id=id)
     return render(request,'user/userdet.html',{'usrlst':usrlst})

def login_view(request,*args,**kwargs):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                print('login success')
                
                return redirect('mobileapp:home')
            else:
                print('login failed')
                messages.error(request, "Invalid username or password")
                
    else:
        form = LoginForm()

    return render(request, 'user/login.html', {'form': form})

def sign_out(request):
     logout(request)
    
     return redirect('customerapp:userlogin')

def home_v(request):
    return render(request, 'user/index1.html')









   

    
