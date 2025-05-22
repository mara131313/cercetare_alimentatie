from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from core.forms import ProductieFermaForm, ProductieFabricaForm, TestCalitateFabricaForm, TestCalitateFermaForm
from users.utils import log_actiune
from core.models import Ferma, Fabrica, ProductieFerma, ProductieFabrica, TestCalitateFerma, TestCalitateFabrica


def adauga_productie_ferma(request):
    if not (request.user.is_superuser or request.user.adauga_produse_alimente or request.user.rol == 'admin'):
        raise PermissionDenied()
    if request.method == 'POST':
        form = ProductieFermaForm(request.POST)
        if form.is_valid():
            form.save()
            user = request.user
            log_actiune(request.user, f"{user.username} a adaugat un aliment.")
            return redirect('success')  # pagina de confirmare
    else:
        form = ProductieFermaForm()
    return render(request, 'core/formular_general.html', {'form': form, 'titlu': 'Adaugă Producție Fermă'})


def adauga_productie_fabrica(request):
    if not (request.user.is_superuser or request.user.adauga_produse_alimente or request.user.rol == 'admin'):
        raise PermissionDenied()
    if request.method == 'POST':
        form = ProductieFabricaForm(request.POST)
        if form.is_valid():
            form.save()
            user = request.user
            log_actiune(request.user, f"{user.username} a adaugat un produs.")
            return redirect('success')
    else:
        form = ProductieFabricaForm()
    return render(request, 'core/formular_general.html', {'form': form, 'titlu': 'Adaugă Producție Fabrică'})


def adauga_test_calitate_fabrica(request):
    if not (request.user.is_superuser or request.user.face_teste or request.user.rol == 'admin'):
        raise PermissionDenied()
    if request.method == 'POST':
        form = TestCalitateFabricaForm(request.POST)
        if form.is_valid():
            form.save()
            user = request.user
            log_actiune(request.user, f"{user.username} a creat un test de calitate pentru o fabrică.")
            return redirect('success')
    else:
        form = TestCalitateFabricaForm()
    return render(request, 'core/formular_general.html', {'form': form, 'titlu': 'Adaugă Test Calitate Fabrica'})


def adauga_test_calitate_ferma(request):
    if not (request.user.is_superuser or request.user.face_teste or request.user.rol == 'admin'):
        raise PermissionDenied()
    if request.method == 'POST':
        form = TestCalitateFermaForm(request.POST)
        if form.is_valid():
            form.save()
            user = request.user
            log_actiune(request.user, f"{user.username} a creat un test de calitate pentru o fermă.")
            return redirect('success')
    else:
        form = TestCalitateFermaForm()
    return render(request, 'core/formular_general.html', {'form': form, 'titlu': 'Adaugă Test Calitate Ferma'})


def vizualizare_date(request):
    context = {
        "ferme": Ferma.objects.all(),
        "fabrici": Fabrica.objects.all(),
        "productii_ferma": ProductieFerma.objects.all(),
        "productii_fabrica": ProductieFabrica.objects.all(),
        "teste_ferma": TestCalitateFerma.objects.all(),
        "teste_fabrica": TestCalitateFabrica.objects.all(),
    }
    return render(request, "core/vizualizare_date.html", context)