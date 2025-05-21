from django import forms
from .models import ProductieFerma, ProductieFabrica, TestCalitateFabrica, TestCalitateFerma

class ProductieFermaForm(forms.ModelForm):
    class Meta:
        model = ProductieFerma
        fields = '__all__'
        labels = {
            'ferma': 'Fermă',
            'data_recoltarii': 'Data recoltării',
            'tip_produs': 'Tip produs',
            'cantitate_kg': 'Cantitate (kg)',
        }

class ProductieFabricaForm(forms.ModelForm):
    class Meta:
        model = ProductieFabrica
        fields = '__all__'
        labels = {
            'fabrica': 'Fabrică',
            'data_productiei': 'Data producției',
            'tip_produs': 'Tip produs',
            'cantitate_kg': 'Cantitate (kg)',
        }

class TestCalitateFabricaForm(forms.ModelForm):
    class Meta:
        model = TestCalitateFabrica
        fields = '__all__'
        labels = {
            'fabrica': 'Fabrică',
            'produs': 'Produs',
            'data_testului': 'Data testului',
            'rezultat_microbiologic': 'Rezultat microbiologic',
            'valori_nutritionale': 'Valori nutriționale',
            'data_expirarii': 'Data expirării',
        }

class TestCalitateFermaForm(forms.ModelForm):
    class Meta:
        model = TestCalitateFerma
        fields = '__all__'
        labels = {
            'ferma': 'Fermă',
            'aliment': 'Aliment',
            'data_testului': 'Data testului',
            'rezultat_microbiologic': 'Rezultat microbiologic',
            'valori_nutritionale': 'Valori nutriționale',
            'data_expirarii': 'Data expirării',
        }

class SelectorForm(forms.Form):
    TIP_SURSA_CHOICES = [
        ('ferma', 'Fermă'),
        ('fabrica', 'Fabrică'),
    ]
    TIP_DATE_CHOICES = [
        ('productie', 'Producție'),
        ('test_calitate', 'Test calitate'),
    ]

    tip_sursa = forms.ChoiceField(choices=TIP_SURSA_CHOICES, label="Tip sursă")
    tip_date = forms.ChoiceField(choices=TIP_DATE_CHOICES, label="Tip date")
