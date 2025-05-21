from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from core.forms import ProductieFermaForm, ProductieFabricaForm, TestCalitateFabricaForm, TestCalitateFermaForm

def adauga_productie_ferma(request):
    if not (request.user.is_superuser or request.user.adauga_produse_alimente or request.user.rol == 'admin'):
        raise PermissionDenied()
    if request.method == 'POST':
        form = ProductieFermaForm(request.POST)
        if form.is_valid():
            form.save()
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
            return redirect('success')
    else:
        form = TestCalitateFermaForm()
    return render(request, 'core/formular_general.html', {'form': form, 'titlu': 'Adaugă Test Calitate Ferma'})