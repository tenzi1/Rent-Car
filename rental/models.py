from django.db import models
from django.urls import reverse

class Car(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='car_images')
    description = models.TextField()
    daily_rent = models.IntegerField()
    is_available = models.BooleanField()
    
    # def get_absolute_url(self):
    #     return reverse('car-details'. kwargs={'pk':self.pk})
