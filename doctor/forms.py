from django import forms
from .models import doctor

class doctor_form(forms.ModelForm):
    class Meta:
        model=doctor
        #fields=('first_name','middle_name','last_name','image','phone_no','mail','address')
        fields="__all__"
        widgets={
            'password1':forms.PasswordInput(),
            'password2':forms.PasswordInput(),
        }

class dr_search(forms.Form):
    search=forms.CharField(max_length=20,label="search the dr list(with respect to name)")
