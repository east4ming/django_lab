from django.urls import path

from django_lab.blog import views

app_name = "blog"
urlpatterns = [
    path("", views.listing, name="listing"),
    path("view_blog/<int:blog_id>/", views.view_blog, name="view_blog"),
    path("see_request/", views.see_request),
    path("user_info/", views.user_info),
]
