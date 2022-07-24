from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path(
        '<slug:blog_slug>/',
        views.blog_details,
        name='blog_details'
        ),
]
