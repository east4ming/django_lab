from django.urls import path

from django_lab.nearbyshops import views

app_name = "nearbyshops"
urlpatterns = [path("", views.home, name="home")]
