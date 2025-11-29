from django.urls import path  # remove include
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>/', views.core_page_detail, name='core_page_detail'),
]
