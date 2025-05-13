from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('', views.selector_view, name='selector'),
    path('productie-ferma/', views.adauga_productie_ferma, name='adauga_productie_ferma'),
    path('productie-fabrica/', views.adauga_productie_fabrica, name='adauga_productie_fabrica'),
    path('test-calitate/', views.adauga_test_calitate, name='adauga_test_calitate'),
    path('success/', lambda request: render(request, 'success.html'), name='success'),
]
