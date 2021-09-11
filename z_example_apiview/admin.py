from django.contrib import admin
from .models import Example1


@admin.register(Example1)
class AdminForApiViewExample(admin.ModelAdmin):
    list_display = ("title", "author", "slug", "created_at")
    prepopulated_fields = {
        "slug": ("title",),
    }


# admin.site.register(AnotherModel)
