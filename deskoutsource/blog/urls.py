from django.urls import path
from .views import (
    blog_list,
    blog_detail,
    blog_category,
    blog_tag,
    blog_search,
)
from .feeds import LatestPostsFeed

app_name = "blog"

urlpatterns = [
    # Blog List (paginated)
    path("", blog_list, name="blog_list"),

    # Search
    path("search/", blog_search, name="blog_search"),

    # Categories
    path("category/<slug:slug>/", blog_category, name="blog_category"),

    # Tags
    path("tag/<slug:slug>/", blog_tag, name="blog_tag"),

    # RSS Feed
    path("feed/", LatestPostsFeed(), name="blog_feed"),

    # Blog Detail Page (must be LAST to avoid conflicts)
    path("<slug:slug>/", blog_detail, name="blog_detail"),
    
]
