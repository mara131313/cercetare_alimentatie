from django.db import models

class Ferma(models.Model):
    nume = models.CharField(max_length=255)
    locatie = models.CharField(max_length=255)
    tip_ferma = models.CharField(max_length=50, choices=[
        ('vegetala', 'Vegetală'),
        ('animala', 'Animalieră'),
        ('mixta', 'Mixtă'),
    ])
    suprafata_ha = models.FloatField(help_text="Suprafață în hectare")
    tipuri_culturi = models.TextField(blank=True, help_text="Ex: grâu, porumb")
    tipuri_animale = models.TextField(blank=True, help_text="Ex: vaci, porci")
    def __str__(self):
        return self.nume

class Fabrica(models.Model):
    nume = models.CharField(max_length=255)
    locatie = models.CharField(max_length=255)
    tipuri_produse = models.TextField(help_text="Ex: lapte, mezeluri")
    certificari = models.TextField(blank=True, help_text="Ex: ISO 22000, BIO")
    def __str__(self):
        return self.nume


class ProductieFerma(models.Model):
    ferma = models.ForeignKey(Ferma, on_delete=models.CASCADE)
    data_recoltarii = models.DateField()
    tip_produs = models.CharField(max_length=100)
    cantitate_kg = models.FloatField()
    fertilizatori = models.TextField(blank=True)
    pesticide = models.TextField(blank=True)
    tip_irigatie = models.CharField(max_length=100, blank=True)
    consum_apa_litri = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.ferma.nume} - {self.tip_produs} ({self.data_recoltarii})"


class ProductieFabrica(models.Model):
    fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE)
    data_productiei = models.DateField()
    produs_final = models.CharField(max_length=100)
    materie_prima = models.TextField(help_text="Tipuri și cantități de materii prime")
    cantitate_produsa_kg = models.FloatField()
    energie_consumata_kwh = models.FloatField()
    deseuri_generate_kg = models.FloatField()

    def __str__(self):
        return f"{self.fabrica.nume} - {self.produs_final} ({self.data_productiei})"


class TestCalitateFabrica(models.Model):
    fabrica = models.ForeignKey(Fabrica, on_delete=models.CASCADE)
    produs = models.CharField(max_length=100)
    data_test = models.DateField()
    rezultat_microbiologic = models.CharField(max_length=255)
    valori_nutritionale = models.TextField(help_text="Ex: calorii, proteine, grăsimi")
    data_expirarii = models.DateField()
    neconformitati = models.TextField(blank=True)

    def __str__(self):
        return f"Test: {self.produs} @ {self.data_test}"


class TestCalitateFerma(models.Model):
    ferma = models.ForeignKey(Ferma, on_delete=models.CASCADE)
    aliment = models.CharField(max_length=100)
    data_testului = models.DateField()
    rezultat_microbiologic = models.CharField(max_length=255)
    valori_nutritionale = models.TextField(help_text="Ex: calorii, proteine, grăsimi")
    data_expirarii = models.DateField()
    neconformitati = models.TextField(blank=True)

    def __str__(self):
        return f"Test: {self.aliment} @ {self.data_testului}"