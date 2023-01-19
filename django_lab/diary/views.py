from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Entry


class EntryListView(LoginRequiredMixin, ListView):
    model = Entry
    queryset = Entry.objects.all().order_by("-date_created")


class EntryDetailView(LoginRequiredMixin, DetailView):
    model = Entry


class EntryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Entry
    fields = ["title", "content"]
    success_url = reverse_lazy("diary:entry-list")
    success_message = "Your new entry was created!"


class EntryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Entry
    fields = ["title", "content"]
    success_message = "Your entry was updated!"

    def get_success_url(self):
        return reverse_lazy("diary:entry-detail", kwargs={"pk": self.object.id})


class EntryDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy("diary:entry-list")
    success_message = "Your entry was deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
