from django.urls import path


from patient.views import formView,p_login

urlpatterns = [
    path('signup/',formView,name='formView'),

    path('login/',p_login,name='p_login'),
]
