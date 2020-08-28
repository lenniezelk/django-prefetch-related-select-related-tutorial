from django.contrib import admin

from .models import Launch, Rocket, Core, Crew


@admin.register(Launch)
class LaunchAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    filter_horizontal = ("crew",)


admin.site.register(Rocket)
admin.site.register(Core)
admin.site.register(Crew)
