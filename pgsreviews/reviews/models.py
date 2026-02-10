

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# PG / Hostel Model
class PG(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    area = models.CharField(max_length=100)
    # 🆕 LOCATION (Google Maps / text)
    location = models.CharField(
        max_length=255,
        blank=True,
        help_text="Google Maps link or landmark"
    )
    monthly_rent = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15)
      # 🆕 PHOTO
    photo = models.ImageField(
        upload_to='pg_photos/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


# Daily Food Menu
class Menu(models.Model):
    pg = models.ForeignKey(PG, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    breakfast = models.CharField(max_length=200)
    lunch = models.CharField(max_length=200)
    dinner = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.pg.name} - {self.date}"


# Reviews & Ratings
class Review(models.Model):
    pg = models.ForeignKey(PG, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_rating = models.IntegerField()
    hygiene_rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pg.name} - {self.user.username}"


# Complaints
class Complaint(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('resolved', 'Resolved'),
    )

    pg = models.ForeignKey(PG, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    ROLE_CHOICES = (
        ('owner', 'Owner'),
        ('resident', 'Resident'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
    

# pg booking

class Booking(models.Model):
    pg = models.ForeignKey('PG', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    move_in_date = models.DateField()
    message = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected')
        ],
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.pg.name} - {self.user.username}"
