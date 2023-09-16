from django.shortcuts import render
from .models import *

# Create your views here.
def news(request):
    new=newss.objects.all().order_by('-date')
    return render(request,'news.html',{'new':new})
