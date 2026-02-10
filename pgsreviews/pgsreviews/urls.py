# """
# URL configuration for pgsreviews project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/6.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path
# from reviews import views
# # from reviews.views import greet

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # pat('hgreet/',greet)
#      path('', views.pg_list, name='pg_list'),

#     path('register/', views.register, name='register'),
#     path('login/', views.user_login, name='login'),
#     path('logout/', views.user_logout, name='logout'),
#     path('owner/', views.owner_dashboard, name='owner_dashboard'),
#     path('resident/', views.resident_dashboard, name='resident_dashboard'),
#     path('owner/menu/<int:pg_id>/', views.add_menu, name='add_menu'),
#     path('pg/<int:pg_id>/', views.pg_detail, name='pg_detail'),
#     path('pg/<int:pg_id>/review/', views.add_review, name='add_review'),
#     path('pg/<int:pg_id>/complaint/', views.add_complaint, name='add_complaint'),
#     path('owner/complaints/', views.owner_complaints, name='owner_complaints'),
#     path('owner/complaint/<int:complaint_id>/resolve/', views.resolve_complaint, name='resolve_complaint'),
# ]


"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from  reviews import views
# from django.contrib import admin
# from django.urls import path
# from cardkeeper import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pg_list, name='pg_list'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('owner/', views.owner_dashboard, name='owner_dashboard'),
    path('resident/', views.resident_dashboard, name='resident_dashboard'),
    path('owner/menu/<int:pg_id>/', views.add_menu, name='add_menu'),
    path('pg/<int:pg_id>/', views.pg_detail, name='pg_detail'),
    path('pg/<int:pg_id>/review/', views.add_review, name='add_review'),
    path('pg/<int:pg_id>/complaint/', views.add_complaint, name='add_complaint'),
    path('owner/complaints/', views.owner_complaints, name='owner_complaints'),
    path('owner/complaint/<int:complaint_id>/resolve/', views.resolve_complaint, name='resolve_complaint'),
    path('pg/<int:pg_id>/book/', views.book_pg, name='book_pg'),
    path('owner/bookings/', views.owner_bookings, name='owner_bookings'),
    path('booking/<int:booking_id>/approve/', views.approve_booking, name='approve_booking'),
    path('booking/<int:booking_id>/reject/', views.reject_booking, name='reject_booking'),

    


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

