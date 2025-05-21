from django.shortcuts import render, redirect
from core.forms import SelectorForm

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
                return redirect('adauga_test_calitate_fabrica')
            elif tip_sursa == 'ferma' and tip_date == 'test_calitate':
                return redirect('adauga_test_calitate_ferma')
    else:
        form = SelectorForm()
    return render(request, 'core/selector_form.html', {'form': form})
