import dis
import json
# import requests
from multiprocessing import context

from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from matrixapp.models import SuperAgent, AddPlot,HOD,BookPlot, CustomUser, Customer,Kyc,Fundtransfer,FundDetails,Installment
from django.contrib import messages
# from django.http import HttpResponse, HttpResponseRedirect
import csv
import datetime


import MySQLdb

# import requests

# import sqlite3 as sql
# from tkinter import *
# from tkinter import ttk
# from tabulate import tabulate


     
 


def about(request):
    return render(request,"default/about.html")

def agents(request):
    return render(request,"default/agents.html")


def services(request):
    return render(request,"default/services.html")

def property(request):
    return render(request,"default/property.html")


def case_study(request):
    return render(request,"default/case-study.html")

def listing(request):
    return render(request,"default/listing.html")

def ind(request):
    return render(request,"default/in.html")

# def about(request):
#     return render(request,"default/about.html")

