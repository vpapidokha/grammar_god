from django.contrib import admin
from .models import *

class TextInline(admin.TabularInline):
    model=Text
    extra=0

class UserAdmin (admin.ModelAdmin):
    list_display=["id", "name", "email", "password"]
    #list_filter=('id',)
    #inlines=[Field]
    inlines = [TextInline]
    search_fields=["id", "name","email"]
    class Meta:
        model=User

admin.site.register(User, UserAdmin)

class TextAdmin (admin.ModelAdmin):
    list_display=["user", "language", "text"]
    search_fields=["language", "text"]

    class Meta:
        model=Text

admin.site.register(Text, TextAdmin)