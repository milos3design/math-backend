from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User, Consent


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # Fields to display in the admin list view
    list_display = ('username', 'email', 'is_active', 'is_staff', 'language_preference')
    list_filter = ('is_active', 'is_staff', 'language_preference')
    search_fields = ('username', 'email')
    ordering = ('username',)

    # Fields to display in the user detail view
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal Info'), {'fields': ('language_preference',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important Dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )


@admin.register(Consent)
class ConsentAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('user', 'consent_given', 'timestamp')
    list_filter = ('consent_given', 'timestamp')
    search_fields = ('user__username', 'user__email')
    ordering = ('-timestamp',)