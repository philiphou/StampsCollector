from django.shortcuts import render
from django.http import HttpResponse
from .models import Stamp

# Create your views here.
def home(request):
    return HttpResponse('<h1> Hello Stamps</h1>')
def about(request):
    return render (request,'about.html')
def stamps_index(request):
    stamps=Stamp.objects.all()
    return render(request,'stamps/index.html',{'stamps':stamps})
def stamps_detail(request,stampid):
    stamp=Stamp.objects.get(id=stampid)
    return render(request,'stamps/detail.html',{'stamp':stamp})
