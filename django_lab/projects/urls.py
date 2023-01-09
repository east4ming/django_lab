from django.urls import path

from django_lab.projects import views

urlpatterns = [
    path("", view=views.project_list),
]
