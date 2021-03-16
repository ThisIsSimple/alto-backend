from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserCreationForm
from .models import CustomUser


class UserAdmin(BaseUserAdmin):
    form = UserCreationForm
    add_form = UserCreationForm

    list_display = ('username', 'email', 'name')
    list_filter = ['is_staff']

    # ordering = ('username')


admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)
