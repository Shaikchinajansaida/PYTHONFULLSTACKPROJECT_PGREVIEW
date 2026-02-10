

# Register your models here.
from django.contrib import admin
from .models import PG, Menu, Review, Complaint,Profile,Booking

admin.site.register(PG)
admin.site.register(Menu)
admin.site.register(Review)
admin.site.register(Complaint)
admin.site.register(Profile)
admin.site.register(Booking)