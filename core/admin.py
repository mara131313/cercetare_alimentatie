from django.contrib import admin
from .models import Ferma, Fabrica, ProductieFerma, ProductieFabrica, TestCalitateFabrica, TestCalitateFerma

admin.site.register(Ferma)
admin.site.register(Fabrica)
admin.site.register(ProductieFerma)
admin.site.register(ProductieFabrica)
admin.site.register(TestCalitateFabrica)
admin.site.register(TestCalitateFerma)
