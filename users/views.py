from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Utilizator

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


def este_admin(user):
    return user.rol == 'admin' or user.is_superuser

@user_passes_test(este_admin)
def gestionare_view(request):
    utilizatori = Utilizator.objects.exclude(id=request.user.id)

    if request.method == "POST":
        actiune = request.POST.get("actiune")
        user_id = request.POST.get("user_id")
        user = get_object_or_404(Utilizator, id=user_id)

        if actiune == "sterge":
            user.delete()
        elif actiune == "promoveaza":
            user.rol = 'admin'
            user.save()
        elif actiune == "update_permisii":
            user.vede_rapoarte = "vede_rapoarte" in request.POST
            user.face_rapoarte = "face_rapoarte" in request.POST
            user.vede_produse_alimente = "vede_produse_alimente" in request.POST
            user.adauga_produse_alimente = "adauga_produse_alimente" in request.POST
            user.vede_teste = "vede_teste" in request.POST
            user.face_teste = "face_teste" in request.POST
            user.save()

        return redirect("gestioneaza_utilizatori")

    return render(request, "core/gestioneaza.html", {"utilizatori": utilizatori})