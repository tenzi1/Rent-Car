from django.urls import path

from .views import CarDetailView, CarHomeView, CarListView, BookCarView
urlpatterns = [
    path('', CarHomeView.as_view(), name='home'),
    path("car/<int:pk>/", CarDetailView.as_view(), name='car-detail'),
    path("car/all/", CarListView.as_view(), name='car-list'),
    path('car/<int:pk>/book/', BookCarView.as_view(), name='book-car'),
]