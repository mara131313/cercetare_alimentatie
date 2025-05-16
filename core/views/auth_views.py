from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        parola = request.POST['password']
        utilizator = authenticate(request, username=username, password=parola)

        if utilizator is not None:
            login(request, utilizator)
            return redirect('home')
        else:
            messages.error(request, 'Date de autentificare incorecte.')

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
    return render(request, 'home.html', {'user': request.user})