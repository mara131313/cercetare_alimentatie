from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from users.utils import log_actiune


@login_required
def raport_view(request):
    if not (request.user.is_superuser or request.user.face_rapoarte or request.user.rol == 'admin'):
        raise PermissionDenied("Nu ai permisiunea să creezi rapoarte.")
    #de adaugat
    user = request.user
    log_actiune(request.user, f"{user.username} a creat un raport.")
    return render(request, 'core/creare_raport.html')