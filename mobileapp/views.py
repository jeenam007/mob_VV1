from django.shortcuts import render, redirect
from django.http import HttpResponse
from mobileapp.forms import ProductCreateForm
from .models import Mobile
from .forms import Mobile

# Create your views here.
def home(request):
    return render(request,'index.html')

def create_product(request):
    if request.method=="GET":
        form=ProductCreateForm()
        return render(request,'create.html',{'form':form})
    
    elif request.method=="POST":
        form=ProductCreateForm(request.POST,files=request.FILES)

    if form.is_valid():
        form.save()
        return redirect('list')
    else:
         return render(request,'create.html',{'form':form})
    
def edit_pdtlist(request,id):
    instance_edit=Mobile.objects.get(id=id)

    if request.POST:
        form=ProductCreateForm(request.POST,request.FILES,instance=instance_edit)
        if form.is_valid():
          form.save()
          return redirect('list')
    else:
        form=ProductCreateForm(instance=instance_edit)
    return render(request, 'create.html', {"form":form})

def list_Products(request):
    pdt=Mobile.objects.all()
    context={'pdt':pdt}
    return render(request,'list.html',context)

def deletepdt(request,id):
    instance=Mobile.objects.get(id=id)
    instance.delete()
    return redirect('list')

def pdt_detail(request, id):
    mobile = Mobile.objects.get(id=id)  # Get the mobile instance or show 404
    return render(request, 'detail.html', {'mobile': mobile})