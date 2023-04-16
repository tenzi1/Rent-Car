from django.contrib import admin

from .models import Car, Booking, Category

admin.site.register(Car)

@admin.register(Booking)
class BookingModelAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'booking_start_date', 'booking_end_date', 'is_approved']
    list_filter = ['is_approved']
    search_fields = ['customer_name']
    list_editable = ['is_approved']

    actions = ['email_customer']

    def email_customer(self, request, queryset):
        for booking in queryset:
            if booking.is_approved:
                email_body = f"""
                    Dear {booking.customer_name},
                    We are pleased to infrom you that your booking has been approved.
                    Thanks
                    Car Rental Service"""
            else:
                email_body = f"""
                    Dear {booking.customer_name},
                    Unfortunately we do not have the capacity right now to accept your booking.
                    Thanks
                    Car Rental Service"""

            print(email_body)
            self.message_user(request, 'Emails were sent successfully')
    email_customer.short_description = 'Send email about booking status to customers'  


                
admin.site.register(Category)