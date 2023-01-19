from django.urls import path

from .views import EntryDetailView, EntryListView

app_name = "diary"
urlpatterns = [
    path("", EntryListView.as_view(), name="entry-list"),
    path("entry/<int:pk>", EntryDetailView.as_view(), name="entry-detail"),
]
