from pyexpat import model
from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Airplane, User, Setting, Booking
from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()
admin.site.register(Airplane)

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['full_name', 'email', 'admin', 'staff']
    list_filter = ['admin','staff']
    fieldsets = (
        (None, {'fields': ('full_name', 'email', 'password')}),
        ('Personal info', {'fields': ('date_of_birth',)}),
        ('Permissions', {'fields': ('admin','staff','active')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name', 'email','password', 'password_2')}
        ),
    )
    search_fields = ['email', 'full_name']
    ordering = ['email']
    filter_horizontal = ()


admin.site.register(User, UserAdmin) 
admin.site.register(Booking) #booking is just added for debugging, remove before production
#booking is just added for debugging, remove before production
@admin.register(Setting)
class BackgroundSettings(admin.ModelAdmin):
    pass
