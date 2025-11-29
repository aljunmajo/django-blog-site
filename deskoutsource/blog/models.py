from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field  # replaced RichTextField import

class BlogCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Blog Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class BlogTag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=60, unique=True)

    class Meta:
        verbose_name_plural = "Blog Tags"
        ordering = ["name"]

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    # SEO Fields
    meta_title = models.CharField(max_length=100)
    meta_description = models.CharField(max_length=200)

    # Blog Core Data
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    excerpt = models.TextField(
        help_text="Short summary for blog listing, SEO, and social previews."
    )

    # Content
    featured_image = models.ImageField(
        upload_to="blog/featured/", blank=True, null=True
    )
    content = CKEditor5Field(
        config_name='default', help_text="Main blog post content using a WYSIWYG editor.", blank=True
    )

    is_featured = models.BooleanField(default=False)

    # Relationships
    category = models.ForeignKey(
        BlogCategory, on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    tags = models.ManyToManyField(BlogTag, blank=True)

    # Publishing
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ["-published_at", "-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
