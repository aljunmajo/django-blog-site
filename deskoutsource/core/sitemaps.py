from django.contrib.sitemaps import Sitemap
from django.urls import reverse, NoReverseMatch
from django.utils import timezone
from django.db.models import Q
from .models import CorePage

class CorePageSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        # Include only published pages; if publish_date is set, ensure it's not in the future
        return (
            CorePage.objects.filter(is_published=True)
            .filter(Q(publish_date__isnull=True) | Q(publish_date__lte=timezone.now()))
        )

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        # Build URL directly to avoid URLConf naming differences
        return "/" if obj.slug == "home" else f"/{obj.slug}/"
