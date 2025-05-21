from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def startup_view(request):
    return render(request, 'registration/startup.html')


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # autentifică automat după signup
            return redirect('home')  # sau altă pagină
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Datele introduse nu sunt corecte.')
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')  # dacă nu e logat, e redirectionat la pagina de login
def home_view(request):
    return render(request, 'home.html')