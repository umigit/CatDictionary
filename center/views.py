from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from extra_views import CreateWithInlinesView, InlineFormSet
from .models import Cat, Image


class CatListView(ListView):
    model = Cat

class ImageListView(ListView):
    model = Image

class CatCreateView(CreateView):
    model = Cat
    fields = ["name"]
    success_url = reverse_lazy("index")

class ImageCreateView(CreateView):
    model = Image
    fields = ["image_original", "latitude", "longitude",]
    
    success_url = reverse_lazy("index")

class ImageInlineFormSet(InlineFormSet):
    model = Image
    fields = ["image_original", "latitude", "longitude",]
    factory_kwargs = {"extra": 1, "can_delete": False}
    # extra = 1
    # can_delete = False

class CatImageCreateFormSetView(CreateWithInlinesView):
    model = Cat
    fields = ["name"]
    inlines = [ImageInlineFormSet]
    template_name = "cat_formset.html"
    success_url = "/"
