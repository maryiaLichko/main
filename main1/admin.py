from django.contrib import admin

# Register your models here.
from main1.models import Teams


class TeamsAdmin(admin.TeamsAdmin):
    model = Teams


admin.site.register(TeamsAdmin)
