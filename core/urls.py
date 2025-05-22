from django.shortcuts import render
from django.urls import path
from core.views.prod_views import vizualizare_date, adauga_productie_ferma, adauga_productie_fabrica, adauga_test_calitate_ferma, adauga_test_calitate_fabrica
from core.views.selector_views import selector_view, selector_date
from core.views.raport_views import raport_view
from core.views.profil_views import profil_view

urlpatterns = [
    path('selector_adauga/', selector_view, name='selector'),
    path("selector/", selector_date, name="selector_date"),
    path("vizualizare/", vizualizare_date, name="vizualizare_date"),
    path('productie-ferma/', adauga_productie_ferma, name='adauga_productie_ferma'),
    path('productie-fabrica/', adauga_productie_fabrica, name='adauga_productie_fabrica'),
    path('test-calitate-fabrica/', adauga_test_calitate_fabrica, name='adauga_test_calitate_fabrica'),
    path('test-calitate-ferma/', adauga_test_calitate_ferma, name='adauga_test_calitate_ferma'),
    path('success/', lambda request: render(request, 'core/success.html'), name='success'),
    path('raport/', raport_view, name='creare_raport'),
    path('profil/', profil_view, name='profil_utilizator'),

]
