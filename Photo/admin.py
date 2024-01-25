from django.contrib import admin
from .models import photo
# Register your models here.
class photoadmin(admin.ModelAdmin):
    list_display=('Name','Photo')
admin.site.register(photo,photoadmin)