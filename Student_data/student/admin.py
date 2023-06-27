from django.contrib import admin
from .models import Student
# Register your models here.

class CustomAdmin(admin.ModelAdmin):
    list_display = ('s_id','s_name','s_age')
    list_display_links = ('s_id','s_name')
admin.site.register(Student, CustomAdmin)