from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('user', 'email', 'profile', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('user', 'email', 'password', 'profile', 'is_admin')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user', 'email', 'profile', 'password1', 'password2')
        }),
    )
    search_fields = ('user',)
    ordering = ('user',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)