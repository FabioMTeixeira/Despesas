from .models import Despesa
from django import forms


class DespesaModelForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'value': forms.NumberInput(attrs={'class': 'form-control'}),
            'bank': forms.Select(attrs={'class': 'form-control'}),
            'month': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
        labels = {
            'name': 'Nome',  # Altera o label de 'name' para 'Nome'
            'value': 'Valor',  # Altera o label de 'value' para 'Valor'
            'bank': 'Banco',  # Altera o label de 'bank' para 'Banco'
            'month': 'Meses',  # Altera o label de 'month' para 'Meses'
            'description': 'Descrição',  # Altera o label de 'description' para 'Descrição'
        }
