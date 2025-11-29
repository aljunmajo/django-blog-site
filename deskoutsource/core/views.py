from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import CorePage

def home(request):
    # Load the CorePage with slug 'home' and render a dedicated template
    home_page = get_object_or_404(CorePage, slug='home')
    return render(request, 'core/home.html', {'core_page': home_page})

def core_page_detail(request, slug):
    # Enforce canonical URL: redirect /home/ to the root URL
    if slug == 'home':
        return redirect('core:home', permanent=True)
    try:
        core_page = get_object_or_404(CorePage, slug=slug)
        return render(request, 'core/core_page_detail.html', {'core_page': core_page})
    except Http404:
        # If a blog post exists with this slug, redirect to its canonical URL
        try:
            from deskoutsource.blog.models import BlogPost  # local import to avoid circular deps
            if BlogPost.objects.filter(slug=slug, is_published=True).exists():
                return redirect('blog:blog_detail', slug=slug)
        except Exception:
            pass
        raise
