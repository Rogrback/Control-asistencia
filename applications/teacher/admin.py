from django.contrib import admin
from .models import Teacher

class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'id_card',
        'first_name',
        'last_name',
        'phone',
        'user',
        'password',
        'user_type'
    )

admin.site.register(Teacher, TeacherAdmin)