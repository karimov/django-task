from django.contrib import admin

# Register your models here.

from .models import School, Classroom, Student

admin.site.register(School)
admin.site.register(Classroom)
admin.site.register(Student)