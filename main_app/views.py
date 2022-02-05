from django.shortcuts import render
from django.http import HttpResponse

class Stamp:
    def __init__(self,name,style,description,release_year):
        self.name=name
        self.style=style
        self.description=description
        self.release_year=release_year

stamps=[
    Stamp('monkey','animal','Chinese Zodiac Monkey',1992),
    Stamp('tiger','animal','Chinese Zodiac tiger',2022),
    Stamp('horse','animal','Chinese Zodiac horse',1990),

]

# Create your views here.
def home(request):
    return HttpResponse('<h1> Hello Stamps</h1>')
def about(request):
    return render (request,'about.html')
def stamps_index(request):
    return render(request,'stamps/index.html',{'stamps':stamps})
