from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def profil_view(request):
    utilizator = request.user
    permisiuni = {
        "Poate genera rapoarte": utilizator.face_rapoarte,
        "Poate vedea produse/alimente": utilizator.vede_produse_alimente,
        "Poate adăuga produse/alimente": utilizator.adauga_produse_alimente,
        "Poate vedea teste": utilizator.vede_teste,
        "Poate efectua teste": utilizator.face_teste,
    }

    return render(request, "core/profil.html", {
        "utilizator": utilizator,
        "permisiuni": permisiuni
    })