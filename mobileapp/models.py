from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Brand(models.Model):
    brand_name=models.CharField(max_length=50,unique=True)

    def __str__(self):
      return self.brand_name

class Mobile(models.Model):
    mobile_name=models.CharField(max_length=70,unique=True)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    price=models.IntegerField()
    specs = models.TextField()
    image=models.ImageField(upload_to='images/')
    date=models.DateField(auto_now=True)

    def __str__(self):
      return self.mobile_name
    
class Cart(models.Model):
   product=models.ForeignKey(Mobile,on_delete=models.CASCADE)
   user=models.CharField(max_length=120)
   quantity = models.PositiveIntegerField(default=1)
   order_id = models.CharField(max_length=100, blank=True, null=True) 
   purchased_date = models.DateTimeField(default=timezone.now)
   STATUS_CHOICES = (
        ("cart", "Cart"),
        ("orderplaced", "Order Placed"),
    )
  
   status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="cart")
   ORDER_STATUS_CHOICES = (
        ('ordered', 'Ordered'),
        ('packed', 'Packed'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    )
   order_status = models.CharField(max_length=50, choices=ORDER_STATUS_CHOICES, default='ordered')
   customer_name=models.CharField(max_length=100,blank=True,null=True)
   address = models.CharField(max_length=300, blank=True, null=True)
   mob_no = models.BigIntegerField(blank=True, null=True)
   email_id=models.EmailField(blank=True,null=True)
   
   def get_total_price(self):
        return self.quantity * self.product.price
   
  