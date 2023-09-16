from django.shortcuts import render
from .models import *
# Create your views here.
def signup(request):
    sign=Signup.objects.all()
    return render(request,'SignUp.html',{'sign':sign})
def login(request):
    user=Signup.objects.all()
    return render(request,'login.html',{'user':user})