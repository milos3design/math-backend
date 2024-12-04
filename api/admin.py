from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import UserCreationForm, UserChangeForm

class UserAdmin(BaseUserAdmin):
    # Forms for adding and changing user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # Fields to display in the admin interface
    list_display = ('username', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')

    # Fieldsets for displaying user details
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser',
                                    'groups', 'user_permissions')}),
    )

    # Fieldsets for adding a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2',
                       'is_staff', 'is_active')}
        ),
    )

    # Fields to use for searching and ordering
    search_fields = ('username', 'email')
    ordering = ('username',)

# Register the custom User model with the admin site
admin.site.register(User, UserAdmin)
