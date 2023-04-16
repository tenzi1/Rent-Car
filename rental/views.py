from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView, View, CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ValidationError
from .models import Car, Booking, Category
from .forms import BookCarForm
class CarHomeView(TemplateView):
    template_name = 'home.html'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'


class AllCarView(ListView):
    model = Car
    template_name = 'car_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
     
        category = Category.objects.get(category__icontains=slug)
        try:
            cars = Car.objects.filter(category=category)
        except Car.DoesNotExist:
            context['car_list'] = None
        context['car_list'] = cars
        return context

class BookCarView(CreateView):
    form_class = BookCarForm
    template_name = 'create_booking.html'
   
    def form_valid(self, form):
        car = Car.objects.get(pk=self.kwargs['pk'])
        booking = form.save()
        booking.car.add(car)
        booking.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self) -> str:
        return reverse('home')


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     car = Car.objects.get(pk=self.kwargs['pk'])
    #     print(self.kwargs)
    #     print(context)
    #     print(kwargs)
    #     return context   
