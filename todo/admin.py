from django.contrib import admin
from .models import Todo
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    model = Todo
    search_fields = ['title']
    list_filter = ['completed']

admin.site.register(Todo, TodoAdmin)