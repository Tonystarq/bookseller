from django.shortcuts import render,HttpResponse
from matrixapp.EmailBackEnd import EmailBackEnd
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    return render(request, "basic.html")


