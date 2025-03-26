from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display =["id", "title", "user", "created_at"]
    list_filter =["created_at", "user"]
    readonly_fieldsd =["id", "created_at"]

admin.site.register(Note, NoteAdmin)
