from django.db import models
from django.contrib.auth.models import User   #author= models.Foreignkey(User, on_delete=models.CASCADE)
import uuid
from django.urls import reverse
from django.utils.html import format_html

# Create your models here.

#contact model 
class Contact(models.Model):
    name=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    subject=models.CharField(max_length=120)
    message=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name+"  "+self.email
      
    # class Meta:
    #     verbose_name_plural="Contact Table"  


# class Category(models.Model):
#     category_name=models.CharField(max_length=100)
# #   category_image=models.ImageField(upload_to='categories') future inhancement mai rakhengy...



class Order(models.Model):
    DELIVERY_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    order_id = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #types=models.ForeignKey(Category,on_delete=models.CASCADE, default='') future inhancement
    quantity = models.IntegerField()
    payment = models.DecimalField(max_digits=8, decimal_places=2)
    paid=models.BooleanField(default=False)
    invoice_number = models.CharField(max_length=50,default='')
    address=models.CharField(max_length=250)
    price=models.CharField(max_length=80)
    delivery_status = models.CharField(max_length=50,choices=DELIVERY_STATUS_CHOICES,default='pending')
    date=models.DateTimeField(auto_now=True)
  


    def __str__(self):
        return f"Order {self.order_id} for {self.user}"

class Price(models.Model):
    price=models.DecimalField(max_digits=8,decimal_places=2)
    # item,description


class stockAvailable(models.Model):
    Stock=models.IntegerField()
    

# class AdminDetails(models.Model):
#     name=models.CharField(max_length=150)
#     mobile=models.CharField(max_length=12)
#     address=models.TextField()
#     description=models.TextField()




      