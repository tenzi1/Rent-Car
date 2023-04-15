from django.urls import path

from .views import CarDetailView, CarHomeView, CarListView

urlpatterns = [
    path('', CarHomeView.as_view(), name='home'),
    path("car/<int:pk>/", CarDetailView.as_view(), name='car-detail'),
    path("car/all/", CarListView.as_view(), name='car-list'),
]