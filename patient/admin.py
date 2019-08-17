from django.contrib import admin
from .models import patient
# Register your models here.
class patientAdmin(admin.ModelAdmin):
    list_display = ('first_name','middle_name','last_name','image','phone_no','mail','address')
    list_filter=('first_name','middle_name','last_name','image','phone_no','mail','address')
admin.site.register(patient, patientAdmin)
