from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('stamps/',views.stamps_index,name='index'),
    path('stamps/<int:stamp_id>',views.stamps_detail,name='detail'),
    path('stamps/create/',views.StampCreate.as_view(),name='stamp_create'),
    path('stamps/<int:pk>/update/',views.StampUpdate.as_view(),name='stamp_update'),
    path('stamps/<int:pk>/delete/',views.StampDelete.as_view(),name='stamp_delete'),
    path('stamps/<int:stamp_id>/add_feature/',views.add_feature,name='add_feature'),
    path('stamps/<int:stamp_id>/add_photo/', views.add_photo, name='add_photo'),
    path('stamps/<int:stamp_id>/assoc_owner/<int:owner_id>/', views.assoc_owner, name='assoc_owner'),
    path('owners/', views.OwnerList.as_view(), name='owners_index'),
    path('owners/<int:pk>/', views.OwnerDetail.as_view(), name='owners_detail'),
    path('owners/create/', views.OwnerCreate.as_view(), name='owners_create'),
    path('owners/<int:pk>/update/', views.OwnerUpdate.as_view(), name='owners_update'),
    path('owners/<int:pk>/delete/', views.OwnerDelete.as_view(), name='owners_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]