from django.urls import path
from users.views import startup_view, login_view, logout_view, signup_view, home_view, gestionare_view, audit_view, test_email
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', startup_view, name='startup'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),
    path('gestionare/', gestionare_view, name='gestionare_utilizator'),
    path("audit/", audit_view, name="audit_log"),
    path('email-test/', test_email, name='email_test'),
    path('resetare-parola/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('resetare-parola/trimis/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('resetare-parola/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('resetare-parola/complet/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]