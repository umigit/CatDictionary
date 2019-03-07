from django.shortcuts import render
from .models import CatData
from django.views.generic import ListView

class CenterListView(ListView):
    model = CatData
