from distutils.command.upload import upload
from pyexpat import model
from tkinter import CASCADE
# from turtle import update
from django.db import models
from django.contrib.auth.models import AbstractUser
# import uuid
from .utils import generate_ref_code

# Create your models here.

class CustomUser(AbstractUser):
    USER = (
        ('1', 'HOD'),
        ('2', 'Agent'),
        # ('3 ', 'Customer'),

    )
    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to = 'media/profile_pic')
    user_id = models.CharField(max_length=12,blank=True)
    pnumber = models.CharField(max_length=12,blank=True)
    address = models.CharField(max_length=12,blank=True)
    

   
    

    def save(self, *args, **kwargs):
        if self.user_id == "":
            user_id = generate_ref_code()
            self.user_id = user_id
        super().save(*args, **kwargs)
class HOD(models.Model):
    
 
    # id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

    def __str__(self):
        return str(self.admin)


    

class SuperAgent(models.Model):
    # code = str(uuid.uuid4()).replace("-", "")[:6]
    # user_id=models.CharField(max_length=50, default=code)
    
    # percentage = models.IntegerField()
    # owner = models.ForeignKey(to=CustomUser,on_delete=models.CASCADE)
    reference_id = models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)   
    objects=models.Manager()

     
    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name
    

class BuyBook(models.Model):
    owner = models.ForeignKey(to=CustomUser,on_delete=models.CASCADE)
    bookname = models.CharField(max_length=10)
    author = models.CharField(max_length=50,null=True,blank=True)
    publishingyear = models.CharField(max_length=50,null=True,blank=True)
    Price = models.BigIntegerField(null=True,blank=True)
    ref_id = models.CharField(max_length=50,null=True,blank=True)
    
    objects=models.Manager()

    
    def __str__(self):
        return self.owner
    
 

class AddBook(models.Model):
    bookname = models.CharField(max_length=10)
    author = models.CharField(max_length=50,null=True,blank=True)
    publishingyear = models.CharField(max_length=50,null=True,blank=True)
    Price = models.BigIntegerField(null=True,blank=True)
    

    objects=models.Manager()

    
    def __str__(self):
        return self.bookname
    


class Customer(models.Model):
    owner = models.ForeignKey(to=CustomUser,on_delete=models.CASCADE)
    VehicleModel = models.CharField(max_length=10)
    VehicleNumber = models.CharField(max_length=50,null=True,blank=True)
    SeatingCapacity = models.CharField(max_length=50,null=True,blank=True)
    RentPerDay = models.BigIntegerField(null=True,blank=True)
    

    objects=models.Manager()

    
    def __str__(self):
        return self.VehicleNumber

