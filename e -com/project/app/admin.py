from django.contrib import admin

# Register your models here.


from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['stu_name', 'stu_email', 'stu_password' ,'stu_password']