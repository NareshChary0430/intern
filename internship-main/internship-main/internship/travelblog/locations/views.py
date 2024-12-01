from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Location
from .forms import LocationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login


def home(request):
    locations = Location.objects.all()  # Adjust this query based on your needs
    return render(request, 'locations/home.html', {'locations': locations})


@login_required
def add_location(request):
    form = LocationForm(data=request.POST or None, files=request.FILES or None)
    if request.method == "POST" and form.is_valid():
        location = form.save(commit=False)
        location.user = request.user
        location.save()
        messages.success(request, "Location added successfully.")
        return redirect('home')
    return render(request, 'locations/add_location.html', {'form': form})

@login_required
def location_view(request):
    locations = Location.objects.filter(user=request.user)
    return render(request, 'locations/locationview.html', {'locations': locations})

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Check if "Remember me" is checked
            if request.POST.get('remember-me'):
                request.session.set_expiry(1209600)  # Two weeks session expiry
            next_url = request.GET.get('next', 'locations')
            return redirect(next_url)
        else:
            messages.error(request, "Invalid credentials")
            return render(request, 'login.html')
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect("home")
