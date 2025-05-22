from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Utilizator, AuditLog
from .utils import log_actiune
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q

# View - uri pentru conectare : pagina de inceput, pagina pentru creerea contului, pagina pentru logare in cont ; si deconectare
def startup_view(request):
    return render(request, 'registration/startup.html')


def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # autentifică automat după signup
            return redirect('home')
    else:
        form = CustomUserCreationForm()
        messages.error(request, 'Datele introduse nu sunt corecte.')
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
# View pentru gestionarea utilizatorilor
@user_passes_test(este_admin)
def gestionare_view(request):
    # Se acceseaza toti utilizatorii in afara de cel conectat la pagina
    utilizatori = Utilizator.objects.exclude(id=request.user.id)

    if request.method == "POST":
        actiune = request.POST.get("actiune")
        user_id = request.POST.get("user_id")
        user = get_object_or_404(Utilizator, id=user_id)

        if actiune == "sterge":
            user.delete()
        elif actiune == "promoveaza":
            #daca user ul e promovat la admin, primeste toate rolurile
            user.rol = 'admin'
            user.face_rapoarte = True
            user.vede_produse_alimente = True
            user.adauga_produse_alimente = True
            user.vede_teste = True
            user.face_teste = True
            user.save()
        elif actiune == "update_permisii":
            # Atribuie valoarea pe care o da administratorul
            user.face_rapoarte = "face_rapoarte" in request.POST
            user.vede_produse_alimente = "vede_produse_alimente" in request.POST
            user.adauga_produse_alimente = "adauga_produse_alimente" in request.POST
            user.vede_teste = "vede_teste" in request.POST
            user.face_teste = "face_teste" in request.POST
            user.save()
            log_actiune(request.user, f"A modificat permisiunile lui {user.username}")

        return redirect("gestionare_utilizator")

    return render(request, "core/gestioneaza.html", {"utilizatori": utilizatori})


# View pentru accesarea paginii in care vor fi vazute activitatile utilizatorilor
def audit_view(request):
    query = request.GET.get("q", "")
    logs = AuditLog.objects.all()
# verifica daca gaseste log-uri in care sa fie incluse username sau actiune
    if query:
        logs = logs.filter(
            Q(actiune__icontains=query) |
            Q(user__username__icontains=query)
        )

    logs = logs.order_by("-timestamp")[:100]  # cele mai recente 100

    return render(request, "core/audit_log.html", {"logs": logs, "query": query})

from django.core.mail import send_mail
from django.http import HttpResponse


#testarea trimiterii mail-ului
def test_email(request):
    send_mail(
        subject='Test Notificare Email',
        message='Acesta este un email de test trimis din platforma Cercetare Alimentație.',
        from_email=None,
        recipient_list=['mara.amv13@gmail.com'],
        fail_silently=False,
    )
    return HttpResponse("Email trimis cu succes!")