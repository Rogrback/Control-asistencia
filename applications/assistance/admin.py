from django.contrib import admin
from .models import Assistance
# Register your models here.

class AssistanceAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'course',
        'date',
        'state'
    )

admin.site.register(Assistance, AssistanceAdmin)