from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'phone', 'email', 'role', 'is_active')
    search_fields = ('first_name', 'role', 'is_active')
    list_filter = ('role',)

