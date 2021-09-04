from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import snackes
# Create your views here.
class SnackListView(ListView):
    template_name = 'snackes_lists.html'
    model = snackes
class SnackDetailsView(DetailView):
    template_name = 'snackes_details.html'
    model = snackes
