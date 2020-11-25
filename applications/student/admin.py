from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'student_enrollment',
        'first_name',
        'last_name',
        'photography',
        'grade'
    )

admin.site.register(Student, StudentAdmin)