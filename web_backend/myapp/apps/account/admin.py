from django.contrib import admin

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

from .models import Account

User = get_user_model()


class EmailUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True


class CustomUserAdmin(UserAdmin):
    list_display = (
        'email',
        'first_name',
        'last_name',
    )
    list_filter = (
        'is_superuser', 'is_staff', 'is_active',
    )
    search_fields = ('email',)
    filter_horizontal = ('user_permissions',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2'),
            'classes': ('wide',)
        }),
        (_('Personal info'), {'fields': ('first_name', 'last_name',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
    )

    add_form = EmailUserCreationForm


admin.site.register(User, CustomUserAdmin)
admin.site.register(Account)
