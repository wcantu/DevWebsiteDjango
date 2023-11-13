from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegistrationForm

# Registration View
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in directly after registration
            messages.success(request, "Registration successful.")
            return redirect('home')  # Redirect to home page after successful registration
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = UserRegistrationForm()
    return render(request, 'registration.html', {'form': form})

# Login View
def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)  # Using email as the username
        if user is not None:
            login(request, user)
            messages.success(request, f"You are now logged in as {email}.")
            return redirect('home')  # Redirect to home page after login
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'sign-in.html')

# Logout View
def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')  # Redirect to login page after logout
