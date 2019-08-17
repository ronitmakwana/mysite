from django.contrib import admin
from .models import doctor

# Register your models here.
class doctorAdmin(admin.ModelAdmin):
    list_display = ('dr_first_name','dr_middle_name','dr_last_name','gender','dr_image','dr_phone_no','dr_mail','dr_degree','dr_speciality','address')
    list_filter=('dr_first_name','dr_middle_name','dr_last_name','gender','dr_image','dr_phone_no','dr_mail','dr_degree','dr_speciality','address')
admin.site.register(doctor, doctorAdmin)
