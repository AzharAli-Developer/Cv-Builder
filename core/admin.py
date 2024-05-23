from django.contrib import admin
from .models import Image
# Register your models here.
class azhar(admin.ModelAdmin):
    list_display = ['name','email','address','photo','doc']
admin.site.register(Image,azhar)