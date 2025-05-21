from django.shortcuts import render
from django.urls import path
from . import views
from users.views import login_view, logout_view, signup_view, home_view

urlpatterns = [
    # path('', views.selector_view, name='selector'),
    path('', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('productie-ferma/', views.adauga_productie_ferma, name='adauga_productie_ferma'),
    path('productie-fabrica/', views.adauga_productie_fabrica, name='adauga_productie_fabrica'),
    path('test-calitate/', views.adauga_test_calitate, name='adauga_test_calitate'),
    path('success/', lambda request: render(request, 'core/success.html'), name='success'),
]
