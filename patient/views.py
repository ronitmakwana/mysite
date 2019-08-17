from django.shortcuts import render,redirect
from .forms import patient_form
from django.http import HttpResponse
# Create your views here.
def formView(request):
    form=patient_form(request.POST,files=request.FILES)
    if form.is_valid():
        form.save()
    else:
        return render(request,'patient_signup_form.html',{'form':form})
    return render(request,'patient/patient_login.html',{})

def p_login(request):
    return render(request,'patient/patient_login.html',{})

