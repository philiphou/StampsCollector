from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Stamp
from .forms import FeatureForm

# Create your views here.
class StampCreate(CreateView):
    model=Stamp
    fields='__all__'



class StampUpdate(UpdateView):
    model=Stamp
    fields='__all__'

class StampDelete(DeleteView):
    model=Stamp
    success_url='/stamps/'
    
def home(request):
    return render (request,"home.html")
def about(request):
    return render (request,'about.html')
def stamps_index(request):
    stamps=Stamp.objects.all()
    return render(request,'stamps/index.html',{'stamps':stamps})
def stamps_detail(request,stamp_id):
    stamp=Stamp.objects.get(id=stamp_id)
    feature_form=FeatureForm()
    return render(request,'stamps/detail.html',{'stamp':stamp,'feature_form':feature_form})
def add_feature(request, stamp_id):
  # create a ModelForm instance using the data in request.POST
  form = FeatureForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feature = form.save(commit=False)
    new_feature.stamp_id = stamp_id
    new_feature.save()
  return redirect('detail', stamp_id=stamp_id)