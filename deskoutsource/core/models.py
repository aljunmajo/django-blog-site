from django.db import models
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field  # Use CKEditor 5 field

class CorePage(models.Model):
    """Model for core pages like About, Services, Contact, etc."""
    meta_title = models.CharField(max_length=100, blank=True)
    meta_description = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=50, unique=True)
    page_title = models.CharField(max_length=30)
    hero_background = models.ImageField(upload_to='core/hero/', blank=True, null=True)
    hero_description = models.TextField(blank=True)
    main_content = CKEditor5Field('Main content', config_name='default', blank=True, help_text=_('WYSIWYG content for the main section'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    featured_image = models.ImageField(upload_to='core/featured/', blank=True, null=True)

 
    class Meta:
        verbose_name = 'Core Page'
        verbose_name_plural = 'Core Pages'

    def __str__(self):
        return self.page_title
