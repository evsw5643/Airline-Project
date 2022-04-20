from django.contrib import admin

from .models import Airplane, User, Setting


admin.site.register(Airplane)


@admin.register(Setting)
class BackgroundSettings(admin.ModelAdmin):
    pass