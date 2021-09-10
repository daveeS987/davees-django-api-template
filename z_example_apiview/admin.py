from django.contrib import admin
from .models import ModelForApiView

# admin.site.register(ModelForApiView)
@admin.register(ModelForApiView)
class AdminForApiViewExample(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
