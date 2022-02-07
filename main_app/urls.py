from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('stamps/',views.stamps_index,name='index'),
    path('stamps/<int:stampid>',views.stamps_detail,name='index'),

]