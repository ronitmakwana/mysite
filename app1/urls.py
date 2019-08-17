from django.urls import path
from .views import home,about,signup,user_profile


urlpatterns = [
    path('home/',home,name='home'),
    path('about/',about),
    path('signup/',signup,name='signup'),
    path('profile/',user_profile),
]
