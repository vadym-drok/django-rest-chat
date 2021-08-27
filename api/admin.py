from django.contrib import admin
from .models import Message
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


# Ad user email in admin
class UserAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email',)}), )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Message)
