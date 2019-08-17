from django.urls import path
from .views import formView,index,home,doctor_list,dr_search_list,searchform

urlpatterns = [
    path('signup/',formView,name='formView'),
    path('index/',index),
    path('home/',home,name='home'),
    path('dr_list/',doctor_list,name='dr_list'),
    path('dr_list/<str:dr_id>',doctor_list,name='dr_search'),
    path('search',searchform),
    path('dr_search_list/',dr_search_list.as_view(),name='drSearchList'),
    
    
]
