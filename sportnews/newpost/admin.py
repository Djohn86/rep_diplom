from django.contrib import admin
from .models import Sportnews, Coment


class NewpostAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)


admin.site.register(Sportnews, NewpostAdmin)
admin.site.register(Coment)


