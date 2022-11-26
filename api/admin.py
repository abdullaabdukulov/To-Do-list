from django.contrib import admin
from .models import Todo

# admin.site.register(Todo)
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'created_at', 'is_finished')