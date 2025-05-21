from django.shortcuts import render
from django.urls import path
from core.views.prod_views import adauga_productie_ferma, adauga_productie_fabrica, adauga_test_calitate_ferma, adauga_test_calitate_fabrica
from core.views.selector_views import selector_view
from core.views.raport_views import raport_view
from users.views import startup_view, login_view, logout_view, signup_view, home_view, gestionare_view, audit_view

urlpatterns = [
    path('', startup_view, name='startup'),

    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),
    path('selector/', selector_view, name='selector'),
    path('productie-ferma/', adauga_productie_ferma, name='adauga_productie_ferma'),
    path('productie-fabrica/', adauga_productie_fabrica, name='adauga_productie_fabrica'),
    path('test-calitate-fabrica/', adauga_test_calitate_fabrica, name='adauga_test_calitate_fabrica'),
    path('test-calitate-ferma/', adauga_test_calitate_ferma, name='adauga_test_calitate_ferma'),
    path('success/', lambda request: render(request, 'core/success.html'), name='success'),
    path('creeaza_raport/', raport_view, name='creeaza_raport'),
    path('profil_utilizator/', selector_view, name='profil_utilizator'),
    path('gestionare_utilizator/', gestionare_view, name='gestionare_utilizator'),
    path("audit/", audit_view, name="audit_log"),

]
