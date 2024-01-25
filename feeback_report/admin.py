from django.contrib import admin
from .models import feedback
# Register your models here.
class feedbackAdmin(admin.ModelAdmin):
    list_display=('CustomerId','Name','Email','feedback')
admin.site.register(feedback,feedbackAdmin)
