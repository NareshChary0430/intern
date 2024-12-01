from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Locations

# User = get_user_model()

# Home view
def home(request):
    locations = Locations.objects.all()
    return render(request, 'home.html', {'locations': locations})
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

# def register_view(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         password = request.POST['password']

#         User = get_user_model()
#         user = User.objects.create_user(
#             email=email,
#             first_name=first_name,
#             last_name=last_name,
#             password=password
#         )
#         return redirect('login')  # Redirect to login page after registration

#     return render(request, 'register.html')


# # Login view
# def login_view(request):
#     if request.user.is_authenticated:
#         return redirect('home')

#     if request.method == "POST":
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(request, username=email, password=password)

#         if user:
#             login(request, user)
#             messages.success(request, "Logged in successfully!")
#             return redirect('home')
#         else:
#             messages.error(request, "Invalid email or password.")
#     return render(request, 'login.html')

# # Logout view
# @login_required
# def logout_view(request):
#     logout(request)
#     messages.success(request, "You have been logged out successfully.")
#     return redirect('login')

# Add location view
@login_required
def locations_add(request):
    if request.method == "POST":
        location_name = request.POST.get('location_name')
        location_description = request.POST.get('location_description')
        location_image = request.FILES.get('location_image')

        Locations.objects.create(
            location_name=location_name,
            location_description=location_description,
            location_image=location_image,
        )
        messages.success(request, "Location added successfully!")
        return redirect('home')
    return render(request, 'locations_add.html')
