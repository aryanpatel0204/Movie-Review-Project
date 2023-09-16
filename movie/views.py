from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    searchTerm=request.GET.get('seachmovie')
    if searchTerm:
        movies=Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies=Movie.objects.all()
    return render(request,'home.html',{'searchTerm':searchTerm,'movies':movies})
#def signup(request):
#    email=request.GET.get('mail')
#    return render(request,'signup.html',{'email':email})
def about(request):
    return render(request,'about.html')
def detail(request,movie_id):
    movie=get_object_or_404(Movie,pk=movie_id)
    return render(request,'detail.html',{'movie':movie})