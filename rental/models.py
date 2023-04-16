from django.db import models
from django.urls import reverse

class Car(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='car_images')
    description = models.TextField()
    daily_rent = models.IntegerField()
    is_available = models.BooleanField()
    
    def get_absolute_url(self):
        return reverse('car-detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.name
    
class Booking(models.Model):
    car = models.ManyToManyField(Car)
    customer_name = models.CharField(max_length=100)
    booking_start_date = models.DateField()
    booking_end_date = models.DateField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Booking for {self.customer_name}'

