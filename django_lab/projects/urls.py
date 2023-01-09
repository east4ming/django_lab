from django.urls import path

from django_lab.projects import views

app_name = "projects"
urlpatterns = [
    path("test", view=views.test),
    path("", view=views.all_projects, name="all_projects"),
    path("<int:pk>", view=views.project_detail, name="project_detail"),
]
