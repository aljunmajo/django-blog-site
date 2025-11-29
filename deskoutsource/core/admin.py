from django.contrib import admin
from .models import CorePage

@admin.register(CorePage)
class CorePageAdmin(admin.ModelAdmin):
    list_display = ('page_title', 'slug', 'is_published', 'publish_date', 'created_at', 'updated_at')
    list_filter = ('is_published',)
    readonly_fields = ('created_at', 'updated_at')
