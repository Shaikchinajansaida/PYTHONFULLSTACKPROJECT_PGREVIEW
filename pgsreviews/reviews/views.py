# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages


# from django.contrib.auth.decorators import login_required
# from .models import PG, Menu, Profile,Review,Complaint
# from django.utils import timezone


# # HOME / PG LIST PAGE
# def pg_list(request):
#     pgs = PG.objects.all()
#     return render(request, 'pg_list.html', {'pgs': pgs})


# # REGISTER
# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         role = request.POST['role']

#         if User.objects.filter(username=username).exists():
#             messages.error(request, 'Username already exists')
#             return redirect('register')

#         user = User.objects.create_user(
#             username=username,
#             email=email,
#             password=password
#         )

#         Profile.objects.create(user=user, role=role)

#         messages.success(request, 'Registration successful. Please login.')
#         return redirect('login')

#     return render(request, 'register.html')

# # LOGIN
# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)

#             profile = Profile.objects.get(user=user)

#             if profile.role == 'owner':
#                 return redirect('owner_dashboard')
#             else:
#                 return redirect('resident_dashboard')

#         else:
#             messages.error(request, 'Invalid credentials')
#             return redirect('login')

#     return render(request, 'login.html')


# # LOGOUT
# def user_logout(request):
#     logout(request)
#     return redirect('login')





# #temporary dahsboards
# from django.contrib.auth.decorators import login_required

# @login_required
# def owner_dashboard(request):
#     profile = Profile.objects.get(user=request.user)

#     # safety check
#     if profile.role != 'owner':
#         return redirect('resident_dashboard')

#     pgs = PG.objects.filter(owner=request.user)

#     return render(request, 'owner_dashboard.html', {'pgs': pgs})


# @login_required
# def resident_dashboard(request):
#     return render(request, 'resident_dashboard.html')




# @login_required
# def add_menu(request, pg_id):
#     profile = Profile.objects.get(user=request.user)

#     if profile.role != 'owner':
#         return redirect('resident_dashboard')

#     pg = PG.objects.get(id=pg_id, owner=request.user)

#     if request.method == 'POST':
#         breakfast = request.POST['breakfast']
#         lunch = request.POST['lunch']
#         dinner = request.POST['dinner']

#         Menu.objects.create(
#             pg=pg,
#             breakfast=breakfast,
#             lunch=lunch,
#             dinner=dinner
#         )

#         return redirect('owner_dashboard')

#     return render(request, 'add_menu.html', {'pg': pg})




# def pg_detail(request, pg_id):
#     pg = PG.objects.get(id=pg_id)
#     menus = Menu.objects.filter(pg=pg).order_by('-date')
#     reviews = Review.objects.filter(pg=pg)

#     return render(
#         request,
#         'pg_detail.html',
#         {
#             'pg': pg,
#             'menus': menus,
#             'reviews': reviews
#         }
#     )



# from django.contrib.auth.decorators import login_required

# @login_required
# def add_review(request, pg_id):
#     profile = Profile.objects.get(user=request.user)

#     if profile.role != 'resident':
#         return redirect('owner_dashboard')

#     pg = PG.objects.get(id=pg_id)

#     if request.method == 'POST':
#         food_rating = request.POST['food_rating']
#         hygiene_rating = request.POST['hygiene_rating']
#         comment = request.POST['comment']

#         Review.objects.create(
#             pg=pg,
#             user=request.user,
#             food_rating=food_rating,
#             hygiene_rating=hygiene_rating,
#             comment=comment
#         )

#         return redirect('pg_detail', pg_id=pg.id)

#     return render(request, 'add_review.html', {'pg': pg})



# from django.contrib.auth.decorators import login_required

# @login_required
# def add_complaint(request, pg_id):
#     profile = Profile.objects.get(user=request.user)

#     if profile.role != 'resident':
#         return redirect('owner_dashboard')

#     pg = PG.objects.get(id=pg_id)

#     if request.method == 'POST':
#         subject = request.POST['subject']
#         description = request.POST['description']

#         Complaint.objects.create(
#             pg=pg,
#             user=request.user,
#             subject=subject,
#             description=description
#         )

#         return redirect('pg_detail', pg_id=pg.id)

#     return render(request, 'add_complaint.html', {'pg': pg})


# @login_required
# def owner_complaints(request):
#     profile = Profile.objects.get(user=request.user)

#     if profile.role != 'owner':
#         return redirect('resident_dashboard')

#     complaints = Complaint.objects.filter(pg__owner=request.user)

#     return render(request, 'owner_complaints.html', {'complaints': complaints})


# @login_required
# def resolve_complaint(request, complaint_id):
#     profile = Profile.objects.get(user=request.user)

#     if profile.role != 'owner':
#         return redirect('resident_dashboard')

#     complaint = Complaint.objects.get(
#         id=complaint_id,
#         pg__owner=request.user
#     )

#     complaint.status = 'resolved'
#     complaint.save()

#     return redirect('owner_complaints')




# from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import PG, Menu, Profile ,Booking
from django.utils import timezone

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import PG,Profile,Complaint

from django.core.mail import send_mail
from django.conf import settings




# HOME / PG LIST PAGE
def pg_list(request):
    pgs = PG.objects.all()
    return render(request, 'pg_list.html', {'pgs': pgs})


# REGISTER
# def register(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']

#         if User.objects.filter(username=username).exists():
#             messages.error(request, 'Username already exists')
#             return redirect('register')

#         user = User.objects.create_user(
#             username=username,
#             email=email,
#             password=password
#         )
#         user.save()

#         messages.success(request, 'Registration successful. Please login.')
#         return redirect('login')

#     return render(request, 'register.html')
# REGISTER
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        Profile.objects.create(user=user, role=role)

        messages.success(request, 'Registration successful. Please login.')
        return redirect('login')

    return render(request, 'register.html')



# LOGIN
# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('pg_list')
#         else:
#             messages.error(request, 'Invalid credentials')
#             return redirect('login')

#     return render(request, 'login.html')
# LOGIN
# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)

#             profile = Profile.objects.get(user=user)

#             if profile.role == 'owner':
#                 return redirect('owner_dashboard')
#             else:
#                 return redirect('resident_dashboard')

#         else:
#             messages.error(request, 'Invalid credentials')
#             return redirect('login')

#     return render(request, 'login.html')

# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(request, username=username, password=password)

#         if user:
#             login(request, user)

#             # 🔴 CHANGE IS HERE
#             return redirect('pg_list')

#     return render(request, 'login.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # Admin → Django Admin
            if user.is_superuser or user.is_staff:
                return redirect('/admin/')

            # User must have profile
            profile = Profile.objects.get(user=user)

            # Owner
            if profile.role == 'owner':
                return redirect('owner_dashboard')

            # Resident
            return redirect('pg_list')

        messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')


# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(request, username=username, password=password)

#         if user:
#             login(request, user)

#             # 👑 ADMIN → DJANGO ADMIN
#             if user.is_superuser or user.is_staff:
#                 return redirect('/admin/')

#             # ⚠️ Normal users MUST have a profile
#             profile = Profile.objects.get(user=user)

#             # 🏠 OWNER
#             if profile.role == 'owner':
#                 return redirect('owner_dashboard')

#             # 👤 RESIDENT
#             return redirect('pg_list')

#         messages.error(request, 'Invalid credentials')

#     return render(request, 'login.html')

# LOGOUT
def user_logout(request):
    logout(request)
    return redirect('pg_list')

from django.contrib.auth.decorators import login_required

# @login_required
# def owner_dashboard(request):
#     return render(request, 'owner_dashboard.html')
@login_required
def owner_dashboard(request):
    profile = Profile.objects.get(user=request.user)

    # safety check
    if profile.role != 'owner':
        return redirect('resident_dashboard')

    pgs = PG.objects.filter(owner=request.user)

    return render(request, 'owner_dashboard.html', {'pgs': pgs})


@login_required
def resident_dashboard(request):
    return render(request, 'resident_dashboard.html')

@login_required
def add_menu(request, pg_id):
    profile = Profile.objects.get(user=request.user)

    if profile.role != 'owner':
        return redirect('resident_dashboard')

    pg = PG.objects.get(id=pg_id, owner=request.user)

    if request.method == 'POST':
        breakfast = request.POST['breakfast']
        lunch = request.POST['lunch']
        dinner = request.POST['dinner']

        Menu.objects.create(
            pg=pg,
            breakfast=breakfast,
            lunch=lunch,
            dinner=dinner
        )

        return redirect('owner_dashboard')

    return render(request, 'add_menu.html', {'pg': pg})


from .models import PG, Menu, Review, Profile

def pg_detail(request, pg_id):
    pg = PG.objects.get(id=pg_id)
    menus = Menu.objects.filter(pg=pg).order_by('-date')
    reviews = Review.objects.filter(pg=pg)

    return render(
        request,
        'pg_detail.html',
        {
            'pg': pg,
            'menus': menus,
            'reviews': reviews
        }
    )


from django.contrib.auth.decorators import login_required

@login_required
def add_review(request, pg_id):
    profile = Profile.objects.get(user=request.user)

    if profile.role != 'resident':
        return redirect('owner_dashboard')

    pg = PG.objects.get(id=pg_id)

    if request.method == 'POST':
        food_rating = request.POST['food_rating']
        hygiene_rating = request.POST['hygiene_rating']
        comment = request.POST['comment']

        Review.objects.create(
            pg=pg,
            user=request.user,
            food_rating=food_rating,
            hygiene_rating=hygiene_rating,
            comment=comment
        )

        return redirect('pg_detail', pg_id=pg.id)

    return render(request, 'add_review.html', {'pg': pg})


from django.contrib.auth.decorators import login_required

@login_required
def add_complaint(request, pg_id):
    profile = Profile.objects.get(user=request.user)

    if profile.role != 'resident':
        return redirect('owner_dashboard')

    pg = PG.objects.get(id=pg_id)

    if request.method == 'POST':
        subject = request.POST['subject']
        description = request.POST['description']

        Complaint.objects.create(
            pg=pg,
            user=request.user,
            subject=subject,
            description=description
        )

        return redirect('pg_detail', pg_id=pg.id)

    return render(request, 'add_complaint.html', {'pg': pg})


@login_required
def owner_complaints(request):
    profile = Profile.objects.get(user=request.user)

    if profile.role != 'owner':
        return redirect('resident_dashboard')

    complaints = Complaint.objects.filter(pg__owner=request.user)

    return render(request, 'owner_complaints.html', {'complaints': complaints})


@login_required
def resolve_complaint(request, complaint_id):
    profile = Profile.objects.get(user=request.user)

    if profile.role != 'owner':
        return redirect('resident_dashboard')

    complaint = Complaint.objects.get(
        id=complaint_id,
        pg__owner=request.user
    )

    complaint.status = 'resolved'
    complaint.save()

    return redirect('owner_complaints')





@login_required
def book_pg(request, pg_id):
    pg = PG.objects.get(id=pg_id)

    if request.method == 'POST':
        move_in_date = request.POST['move_in_date']
        message = request.POST.get('message', '')

        Booking.objects.create(
            pg=pg,
            user=request.user,
            move_in_date=move_in_date,
            message=message
        )

        return redirect('pg_detail', pg_id=pg.id)

    return render(request, 'book_pg.html', {'pg': pg})





@login_required
def approve_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    booking.status = 'approved'
    booking.save()

    send_mail(
        subject='PG Booking Approved 🎉',
        message=f"""
Hello {booking.user.username},

Good news! 🎉
Your booking for {booking.pg.name} has been APPROVED.

Move-in Date: {booking.move_in_date}

Thank you,
PG Management
""",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[booking.user.email],
        fail_silently=False,
    )

    return redirect('owner_bookings')


@login_required
def reject_booking(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    booking.status = 'rejected'
    booking.save()

    send_mail(
        subject='PG Booking Rejected',
        message=f"""
Hello {booking.user.username},

We’re sorry to inform you that your booking for {booking.pg.name}
has been REJECTED.

You may explore other PGs on the platform.

Thank you,
PG Management
""",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[booking.user.email],
        fail_silently=False,
    )

    return redirect('owner_bookings')




from .models import Booking

# def owner_bookings(request):
#     bookings = Booking.objects.filter(
#         pg__owner=request.user
#     ).order_by('-created_at')

#     return render(
#         request,
#         'Pg_reviews/owner_bookings.html',
#         {'bookings': bookings}
#     )

# @login_required
# def owner_bookings(request):
#     bookings = Booking.objects.filter(pg__owner=request.user)
#     return render(request, 'owner_bookings.html', {'bookings': bookings})

# from .models import Booking, Profile
# from django.contrib.auth.decorators import login_required

@login_required
def owner_bookings(request):
    profile = Profile.objects.get(user=request.user)

    # Only owners allowed
    if profile.role != 'owner':
        return redirect('pg_list')

    # Get bookings for owner’s PGs
    bookings = Booking.objects.filter(
        pg__owner=request.user
    ).order_by('-created_at')

    return render(
        request,
        'owner_bookings.html',
        {'bookings': bookings}
    )



# @login_required
# def approve_booking(request, booking_id):
#     booking = Booking.objects.get(id=booking_id)

#     if booking.pg.owner != request.user:
#         return redirect('owner_dashboard')

#     booking.status = 'approved'
#     booking.save()

#     return redirect('owner_bookings')


# @login_required
# def reject_booking(request, booking_id):
#     booking = Booking.objects.get(id=booking_id)

#     if booking.pg.owner != request.user:
#         return redirect('owner_dashboard')

#     booking.status = 'rejected'
#     booking.save()

#     return redirect('owner_bookings')
