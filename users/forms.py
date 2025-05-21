from django.contrib.auth.forms import UserCreationForm
from .models import Utilizator

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Utilizator
        fields = ['username', 'email', 'password1', 'password2']
