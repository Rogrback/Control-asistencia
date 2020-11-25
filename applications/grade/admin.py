from django.contrib import admin
from .models import Grade
# Register your models here.

class GradeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )

admin.site.register(Grade, GradeAdmin)
