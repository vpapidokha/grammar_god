from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

class TextInline(admin.TabularInline):
    model=Text
    extra=0



class TextAdmin (admin.ModelAdmin):
    list_display=["id", "session_key", "language", "textInputed", "textChecked", "textSuggestion", "dateTimeCreated", "dateTimeDelete"]
    search_fields=["session_key", "language", "textInputed", "textChecked", "textSuggestion", "dateTimeCreated", "dateTimeDelete"]

    class Meta:
        model=Text

admin.site.register(Text, TextAdmin)
