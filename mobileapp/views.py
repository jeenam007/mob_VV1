from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from mobileapp.forms import ProductCreateForm
from .models import Mobile,Cart
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from .decorators import login_required
import uuid
from django.utils import timezone
from collections import defaultdict
from django.core.paginator import Paginator



# Create your views here.
@login_required
def home(request):
    mob=Mobile.objects.all()
    return render(request, 'mobile/index.html',{'mob':mob})


def create_product(request):
    if request.method=="GET":
        form=ProductCreateForm()
        return render(request,'mobile/create.html',{'form':form})
    
    elif request.method=="POST":
        form=ProductCreateForm(request.POST,files=request.FILES)
        messages.success(request, "Product created successfully!")
        if form.is_valid():
            form.save()

            return redirect('mobileapp:list')
        else:
            
            return render(request,'mobile/create.html',{'form':form})
    

def edit_pdtlist(request,id):
    instance_edit=Mobile.objects.get(id=id)

    if request.POST:
        form=ProductCreateForm(request.POST,request.FILES,instance=instance_edit)
        if form.is_valid():
          form.save()
          return redirect('mobileapp:list')
    else:
        form=ProductCreateForm(instance=instance_edit)
    return render(request, 'mobile/create.html', {"form":form})


def list_Products(request):
    pdt=Mobile.objects.all()
    paginator = Paginator(pdt, 6) 

    page_number = request.GET.get('page')  # Get the current page number from the URL
    page_obj = paginator.get_page(page_number)  # Get page object

    context={'page_obj':page_obj}
    return render(request,'mobile/list.html',context)





def deletepdt(request,id):
    instance=Mobile.objects.get(id=id)
    instance.delete()
    messages.success(request, "Product deleted successfully!")
    return redirect('mobileapp:list')

@login_required
def pdt_detail(request, id):
    mobile = Mobile.objects.get(id=id)  # Get the mobile instance or show 404
    return render(request, 'mobile/detail.html', {'mobile': mobile})

@login_required
def add_to_cart(request, id):
        product = get_object_or_404(Mobile, id=id)

        cart_item, created = Cart.objects.get_or_create(
        product=product,
        user=request.user.username, 
        status="cart",
        defaults={'quantity': 1})
    

        if not created:
            cart_item.quantity += 1
            cart_item.save()   
        else:
         print("Item added to cart.")
        return redirect('mobileapp:viewcart') 


@login_required
def my_cart(request):
    cart_items=Cart.objects.filter(user=request.user,status='cart')
    total_price = sum(item.quantity * item.product.price for item in cart_items)
    return render(request, 'mobile/cartpage.html', {
        'cart_items': cart_items,
        'total_price': total_price
        })


    
@login_required
def remove_from_cart(request,id):
    instance=Cart.objects.get(id=id)
    instance.delete()
    return redirect('mobileapp:viewcart')

@login_required
def decrease_quantity(request,id):
    cart_item = get_object_or_404(
         Cart,
        product__id=id,
        user=request.user.username,  # Use request.user if it's a ForeignKey
        status="cart"
    )
    if cart_item.quantity>1:
       cart_item.quantity -= 1
       cart_item.save()
    else:
       cart_item.delete()
    return redirect('mobileapp:viewcart')

@login_required
def place_order(request, id):
    if request.method == "POST":
        customer_name=request.POST.get('customer_name')
        address = request.POST.get("address")
        mob_no=request.POST.get('mob_no')
        email_id=request.POST.get('email_id')
        cart_item = Cart.objects.filter(user=request.user, status='cart')
        if not cart_item.exists():
            return redirect('mobileapp:viewcart')
        
        order_id = str(uuid.uuid4())[:8]  # Unique order ID
        purchased_date = cart_item[0].purchased_date
        # Update the status to "orderplaced"
        for item in cart_item:
            item.status = 'orderplaced'
            item.purchased_date=purchased_date
            item.address=address
            item.order_id = order_id
            item.customer_name=customer_name
            item.mob_no=mob_no
            item.email_id=email_id
            item.save()
            print(order_id)
        return redirect('mobileapp:order_status')
    return render(request, 'mobile/placeorder.html')

@login_required
def order_status(request):
    if request.user.is_superuser:
        orders = Cart.objects.filter(
    status__in=['orderplaced', 'cancelled'],
    ).order_by('-purchased_date')

    else:
        orders = Cart.objects.filter(
    status__in=['orderplaced', 'cancelled'],
    user=request.user
    ).order_by('-purchased_date')

    # Get all items with status 'orderplaced' for this user
    
    grouped_orders = defaultdict(list)

    for item in orders:
        grouped_orders[item.order_id].append(item)

    
    summary = []
    

    for order_id, items in grouped_orders.items():
        total = sum(i.quantity * i.product.price for i in items)
        purchased_date = items[0].purchased_date if items else ""      
        summary.append({
            'purchased_date': purchased_date,
            'order_id': order_id,
            'items': items,
            'total': total,
            'username':items[0].user,
            'customer_name':items[0].customer_name,
            'mob_no':items[0].mob_no,
            'email_id':items[0].email_id,
            'address':items[0].address,
            'status':items[0].status if items else 'NA',
        })

    return render(request, 'mobile/orderstatus.html', {'orders': summary})
def cancel_order(request, order_id):
    # Find all matching cart items for this order
    
    carts = Cart.objects.filter(order_id=order_id, user=request.user, status='orderplaced')

    if carts.exists():
        carts.update(status='cancelled')
        messages.success(request, "Order cancelled successfully!")
    else:
        messages.warning(request, "No matching order found to cancel.")

    return redirect('mobileapp:order_status')
