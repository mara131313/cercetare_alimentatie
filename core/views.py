from django.shortcuts import render, redirect
from .forms import SelectorForm, ProductieFermaForm, ProductieFabricaForm, TestCalitateForm

def selector_view(request):
    if request.method == 'POST':
        form = SelectorForm(request.POST)
        if form.is_valid():
            tip_sursa = form.cleaned_data['tip_sursa']
            tip_date = form.cleaned_data['tip_date']

            # Redirecționează în funcție de combinație
            if tip_sursa == 'ferma' and tip_date == 'productie':
                return redirect('adauga_productie_ferma')
            elif tip_sursa == 'fabrica' and tip_date == 'productie':
                return redirect('adauga_productie_fabrica')
            elif tip_sursa == 'fabrica' and tip_date == 'test_calitate':
                return redirect('adauga_test_calitate')
    else:
        form = SelectorForm()
    return render(request, 'selector_form.html', {'form': form})


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
