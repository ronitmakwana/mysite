from django import forms
from .models import patient

class patient_form(forms.ModelForm):
    class Meta:
        model=patient
        #fields=('first_name','middle_name','last_name','image','phone_no','mail','address')
        fields="__all__"
        widgets={
            'password1':forms.PasswordInput(),
            'password2':forms.PasswordInput(),
        }