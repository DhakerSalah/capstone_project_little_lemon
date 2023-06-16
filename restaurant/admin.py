from django.contrib import admin

# Register your models here.
from .models import Menu, Boking

class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_item', 'inventory')

admin.site.register(Menu, MenuAdmin)
admin.site.register(Boking)