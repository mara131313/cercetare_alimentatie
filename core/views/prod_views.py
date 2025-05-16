from django.shortcuts import render, redirect
from core.forms import ProductieFermaForm, ProductieFabricaForm, TestCalitateForm

def adauga_productie_ferma(request):
    if request.method == 'POST':
        form = ProductieFermaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # pagina de confirmare
    else:
        form = ProductieFermaForm()
    return render(request, 'formular_general.html', {'form': form, 'titlu': 'Adaugă Producție Fermă'})


def adauga_productie_fabrica(request):
    if request.method == 'POST':
        form = ProductieFabricaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ProductieFabricaForm()
    return render(request, 'formular_general.html', {'form': form, 'titlu': 'Adaugă Producție Fabrică'})


def adauga_test_calitate(request):
    if request.method == 'POST':
        form = TestCalitateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = TestCalitateForm()
    return render(request, 'formular_general.html', {'form': form, 'titlu': 'Adaugă Test Calitate'})
