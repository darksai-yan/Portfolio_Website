from django.shortcuts import render

from myapp.models import ArtWork
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.
class MainPage(ListView):
    model = ArtWork
    template_name = 'myapp/artwork_list.html'
    context_object_name = 'artworks'
    ordering = ['-date']