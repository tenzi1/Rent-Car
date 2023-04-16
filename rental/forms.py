from datetime import date
from django.core.exceptions import ValidationError
from django import forms
from django.forms.widgets import DateInput
from .models import Booking

class BookCarForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'booking_start_date', 'booking_end_date']
        widgets = {
            'booking_start_date': DateInput(attrs={'type':'date'}),
            'booking_end_date': DateInput(attrs={'type': 'date'})
        }

    def clean(self):
        cleaned_data = super().clean()
        booking_start_date = cleaned_data.get('booking_start_date')
        booking_end_date = cleaned_data.get('booking_end_date')

        if booking_start_date < date.today() or booking_end_date < booking_start_date:
            raise ValidationError(
                "'booking_start_date' and 'booking_end_date' must not be past date."
            )