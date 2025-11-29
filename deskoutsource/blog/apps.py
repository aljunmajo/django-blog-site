from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # Full Python path to the app (nested inside the project package)
    name = 'deskoutsource.blog'
    verbose_name = 'Blog'
