from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView

from .models import Car

class CarHomeView(TemplateView):
    template_name = 'home.html'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'
