from django.contrib import admin
from testapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['firstname','lasttname','email','password','occupation','dob','image','gender','state','country','education']

admin.site.register(Student,StudentAdmin)
