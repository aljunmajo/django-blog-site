from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import BlogPost

class LatestPostsFeed(Feed):
	"""RSS/Atom feed for the latest published blog posts."""
	title = "DeskOutsource Blog - Latest Posts"
	link = "/blog/"
	description = "Latest published posts from the DeskOutsource blog."

	def items(self):
		return (
			BlogPost.objects.filter(is_published=True)
			.order_by("-published_at", "-created_at")[:20]
		)

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		# Use excerpt; fall back to meta_description if needed
		return item.excerpt or item.meta_description

	def item_link(self, item):
		return reverse("blog_detail", args=[item.slug])
