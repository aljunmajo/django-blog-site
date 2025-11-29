from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap

# Sitemaps
from deskoutsource.blog.sitemaps import BlogPostSitemap
from deskoutsource.core.sitemaps import CorePageSitemap

# RSS Feed
from deskoutsource.blog.feeds import LatestPostsFeed

sitemaps = {
    "blog": BlogPostSitemap,
    "pages": CorePageSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),

    # CKEditor 5
    path('ckeditor5/', include('django_ckeditor_5.urls')),

    # RSS Feed (blog)
    path("blog/feed/", LatestPostsFeed(), name="blog_feed"),

    # Blog URLs
    path("blog/", include("deskoutsource.blog.urls")),

    # Sitemap.xml
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django_sitemap"
    ),

    # Core Pages (kept last because of slug matching)
    path("", include("deskoutsource.core.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
