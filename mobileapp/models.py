from django.db import models
from django.contrib.auth.models import User

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
   STATUS_CHOICES = (
        ("cart", "Cart"),
        ("orderplaced", "Order Placed"),
    )
  
   status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="cart")
  #  def __str__(self):
  #       return f"{self.user} - {self.product.name} ({self.status})"
   def get_total_price(self):
        return self.quantity * self.product.price
