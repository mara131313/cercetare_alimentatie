from django.contrib.auth.forms import UserCreationForm
from .models import Utilizator

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Utilizator
        fields = ['username', 'email', 'rol', 'password1', 'password2']
