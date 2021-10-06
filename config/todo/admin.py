from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Todolist



class Todo(admin.ModelAdmin):
    list_display = ('title', 'created', 'status', )

admin.site.register(Todolist, Todo)