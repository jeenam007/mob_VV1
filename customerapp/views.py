from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm,User


# Create your views here.
def registration(request):
    
    if request.method =="POST":
     form=UserRegistrationForm(request.POST)
     if form.is_valid():
          form.save()
          return redirect("customerapp:userlist")
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
          return redirect('customerapp:userlist')
     else:
          form=UserRegistrationForm(instance=instance_edituser)
          return render(request,'user/registration.html',{'form':form})


     
def userdelete(request,id):
     instance=User.objects.get(id=id)
     instance.delete()
     return redirect('customerapp:userlist')

def userdet(request,id):
     return HttpResponse("<h1>view</h1>")

   

    
