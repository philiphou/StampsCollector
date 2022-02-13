from django.shortcuts import render,redirect
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Stamp, Owner
from .forms import FeatureForm
S3_BASE_URL = 'https://s3.amazonaws.com/'
BUCKET = 'philipstamps'
import uuid
import boto3
from .models import Stamp, Owner, Photo


def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

# Create your views here.
class StampCreate(LoginRequiredMixin,CreateView):
    model=Stamp
    fields=['name','style','description','country']
    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
      form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
      return super().form_valid(form)

def add_photo(request, stamp_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, stamp_id=stamp_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', stamp_id=stamp_id)

class StampUpdate(LoginRequiredMixin,UpdateView):
    model=Stamp
    fields=['name','style','description','country']

class StampDelete(LoginRequiredMixin,DeleteView):
    model=Stamp
    success_url='/stamps/'
    
def home(request):
    return render (request,"home.html")
def about(request):
    return render (request,'about.html')

@login_required    
def stamps_index(request):

    stamps=Stamp.objects.filter(user=request.user)
    return render(request,'stamps/index.html',{'stamps':stamps})
@login_required
def stamps_detail(request,stamp_id):
    stamp=Stamp.objects.get(id=stamp_id)
    owners_stamp_doesnt_have = Owner.objects.exclude(id__in = stamp.owners.all().values_list('id'))
    feature_form=FeatureForm()
    return render(request,'stamps/detail.html',{'stamp':stamp,'feature_form':feature_form,'owners':owners_stamp_doesnt_have})
@login_required
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

@login_required
def assoc_owner(request, stamp_id, owner_id):
  Stamp.objects.get(id=stamp_id).owners.add(owner_id)
  return redirect('detail', stamp_id=stamp_id)

@login_required
def unassoc_owner(request, stamp_id, owner_id):
  Stamp.objects.get(id=stamp_id).owners.remove(owner_id)
  return redirect('detail', stamp_id=stamp_id)

class OwnerList(ListView):
  model = Owner

class OwnerDetail(LoginRequiredMixin,DetailView):
  model = Owner

class OwnerCreate(LoginRequiredMixin,CreateView):
  model = Owner
  fields = '__all__'

class OwnerUpdate(LoginRequiredMixin,UpdateView):
  model = Owner
  fields = ['name', 'postcode']

class OwnerDelete(LoginRequiredMixin,DeleteView):
  model = Owner
  success_url = '/owners/'