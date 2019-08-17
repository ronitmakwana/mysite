from django.shortcuts import render,redirect
from .forms import doctor_form,dr_search
from .models import doctor
from django import views
# Create your views here.
def doctor_list(request,dr_id=None):
    return render(request,'doctor/dr_list.html',{'dr_list':doctor.objects.all() if dr_id == None else doctor.objects.filter(address__icontains = dr_id)})

class dr_search_list(views.View):

    def get(self, request, *args, **kwargs):
        form=dr_search(initial={'search' : 'search name'})
        return render(request,'doctor/dr_search_form.html',{'form': form})

    def post(self, request, *args, **kwargs):
        form=dr_search(data=request.POST)
        if form.is_valid():
            return redirect('doctor:dr_search',dr_id=form.cleaned_data['search'])
        else:
            return render(request,'doctor/dr_search_form.html',{'form': form})

def searchform(request, *args, **kwargs):
    form2=dr_search(initial={'search' : 'search name'})
    return render(request,'doctor/dr_list.html',{'form2': form2})


def formView(request):
    form=doctor_form(request.POST,files=request.FILES)
    if form.is_valid():
        form.save()
    else:
        return render(request,'dr_signup.html',{'form':form})
    return render(request,'doctor/dr_list.html')
def index(request):
    return render(request,'doctor/index.html',{})

def home(request):
    return render(request,'doctor/dr_list.html',{})
