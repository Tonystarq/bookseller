import email
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from matrixapp import views
from MatrixProject import settings

from .import *
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from matrixapp.models import *
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
import csv
import datetime


@login_required(login_url='/')
def Home(request):
    

    return render(request, 'AGENT/home.html')
def view_book1(request):
    bookname = AddBook.objects.all()
    return render(request,'AGENT/view_book1.html',{'bookname':bookname})
    
@login_required(login_url='/')
def  buybook(request, id):

    bookname = AddBook.objects.filter(id=id)
    current_user = request.user
    code = current_user.user_id
    context = {
        'code':code,
        'bookname':bookname

        
    }
        

    return render(request, 'AGENT/buybook.html', context)

def  buybook1(request):
    if request.method == "POST":
        bookname = request.POST.get('bookname')
        
       
        
        author = request.POST.get('author')
        publishingyear =request.POST.get('publishingyear')
        Price = request.POST.get('Price')
        ref_id = request.POST.get('ref_id')
      
           
        buybook = BuyBook(bookname= bookname,author = author, publishingyear = publishingyear,Price=Price,ref_id=ref_id)
        owner=buybook.owner=request.user
           
            
        buybook.owner = owner
       
       
        
           


        
            
        buybook.save()
        
            
        messages.success(request,"Book bought Successfully")
        return redirect('view_book1')
        
    return render(request, 'AGENT/view_book1.html')

def soldbooks(request):
    bookname = BuyBook.objects.all()
    
    current_user = request.user

    Agent_code = current_user
    code = Agent_code.user_id
    context = {
        'customer' : bookname,
        'code' : code
    }

   
    return render(request,'AGENT/soldbooks.html',context)

def booksbought(request):
    bookname = BuyBook.objects.filter(owner=request.user.id)
    current_user = request.user
    # owner=request.user.id
    # print(owner)
    
    # bookname = BuyBook.objects.all()
    
    current_user = request.user

    Agent_code = current_user
    code = Agent_code.user_id
    context = {
        'customer' : bookname,
        'code' : code
    }

   
    return render(request,'AGENT/booksbought.html',context)