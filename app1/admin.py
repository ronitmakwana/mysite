from django.contrib import admin
from .models import product

# Register your models here.
class productAdmin(admin.ModelAdmin):
    list_display = ('p_name','p_price')
    list_filter=('p_name','p_price')
admin.site.register(product, productAdmin)
