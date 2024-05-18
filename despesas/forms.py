from .models import Despesa
from django import forms


class DespesaModelForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = '__all__'
