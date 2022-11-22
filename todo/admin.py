from django.contrib import admin
from todo.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    list_display = ('fullname', 'email', 'is_admin', 'id',)
    search_fields = ('fullname',)
    list_filter = ('joined_at',)
    ordering = ('id', 'fullname', 'email')
    filter_horizontal = ()

    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password',)}),
        ('Personal Info', {'fields': ('fullname', 'picture',)}),
        ('Others', {'fields': ('is_active', 'is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('fullname', 'email', 'picture', 'password1', 'password2'),
        }),
    )
admin.site.register(User, UserAdmin)