from pyexpat import model
from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Airplane, User, Setting


User = get_user_model()
admin.site.register(Airplane)

class UserAdmin(admin.ModelAdmin):
    search_fields = ["email"]
    class Meta:
        model = User

admin.site.register(User, UserAdmin)

@admin.register(Setting)
class BackgroundSettings(admin.ModelAdmin):
    pass