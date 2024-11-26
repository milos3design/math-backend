from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserAccount

@admin.register(UserAccount)
class CustomUserAdmin(UserAdmin):
    model = UserAccount
    list_display = ('id', 'username', 'email', 'is_staff', 'is_superuser', 'is_active')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('username',)