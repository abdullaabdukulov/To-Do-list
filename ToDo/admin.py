from django.contrib import admin
from .models import Todo, TodoList


@admin.register(Todo)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('description', 'creator', 'todolist', 'created_at', 'finished_at', 'is_finished')
    list_filter = ('is_finished', 'creator')


