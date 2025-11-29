from django.shortcuts import render, get_object_or_404
from .models import BlogPost, BlogCategory, BlogTag

# def blog_list(request):
#     posts = BlogPost.objects.filter(is_published=True)
#     return render(request, "blog/post_list.html", {"posts": posts})

from django.core.paginator import Paginator

def blog_list(request):
    posts = BlogPost.objects.filter(is_published=True)
    paginator = Paginator(posts, 10)  # 10 posts per page

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "blog/post_list.html", {"page_obj": page_obj})



# def blog_detail(request, slug):
#     post = get_object_or_404(BlogPost, slug=slug, is_published=True)
#     return render(request, "blog/post_detail.html", {"post": post})

def blog_detail(request, slug):
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)

    next_post = None
    prev_post = None

    if post.published_at:
        next_post = (
            BlogPost.objects.filter(
                published_at__gt=post.published_at,
                is_published=True,
                published_at__isnull=False,
            )
            .order_by("published_at")
            .first()
        )

        prev_post = (
            BlogPost.objects.filter(
                published_at__lt=post.published_at,
                is_published=True,
                published_at__isnull=False,
            )
            .order_by("-published_at")
            .first()
        )

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "next_post": next_post,
            "prev_post": prev_post,
        },
    )



def blog_category(request, slug):
    category = get_object_or_404(BlogCategory, slug=slug)
    posts = category.posts.filter(is_published=True)
    return render(request, "blog/category_list.html", {
        "category": category,
        "posts": posts
    })



from django.db.models import Q

def blog_search(request):
    query = (request.GET.get("q", "") or "").strip()
    posts = BlogPost.objects.none()

    if query:
        posts = BlogPost.objects.filter(
            Q(title__icontains=query)
            | Q(excerpt__icontains=query)
            | Q(content__icontains=query),
            is_published=True,
        )

    return render(request, "blog/search.html", {"posts": posts, "query": query})


def blog_tag(request, slug):
    tag = get_object_or_404(BlogTag, slug=slug)
    posts = BlogPost.objects.filter(tags=tag, is_published=True)
    return render(request, "blog/tag_list.html", {"tag": tag, "posts": posts})

