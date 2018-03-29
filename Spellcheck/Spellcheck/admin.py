from django.contrib import admin
from .models import *

class UserAdmin (admin.ModelAdmin):
    list_display=["id", "name", "email", "password"]
    #list_filter=('id',)
    #inlines=[Field]
    search_fields=["id", "name","email"]
    class Meta:
        model=User

admin.site.register(User, UserAdmin)