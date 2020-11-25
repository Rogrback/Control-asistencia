from django.contrib import admin
from .models import UserType
# Register your models here.

class UserTypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )

admin.site.register(UserType, UserTypeAdmin)