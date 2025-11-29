from django.contrib import admin
from .models import BlogPost, BlogCategory, BlogTag

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_published", "published_at")
    list_filter = ("is_published", "category", "tags")
    search_fields = ("title", "excerpt", "meta_title")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("tags",)

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
