from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CreateUserForm, EmailAuthenticationForm
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # Load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.height = form.cleaned_data.get('height')
            user.profile.weight = form.cleaned_data.get('weight')
            user.profile.dropdown_field = form.cleaned_data.get('dropdown_field')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            
            # Authenticate the user after registration
            user = authenticate(username=user.username, password=raw_password)
            if user is not None:
                login(request, user)  # Log in the user
                return redirect('login')  # Redirect to the success page after login
    else:
        form = CreateUserForm()
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Correct usage of login function
                return redirect('home')  # Redirect to the home page after login
    else:
        form = EmailAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    return render(request, 'home.html')