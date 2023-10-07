from django.contrib import admin
from .models import Sportnews


class NewpostAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(Sportnews, NewpostAdmin)


