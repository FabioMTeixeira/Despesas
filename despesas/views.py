from despesas.forms import DespesaModelForm
from .models import Despesa, Bank, Month, DespesaMensal
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Sum

# Create your views here.


class MonthlyExpensesListView(ListView):
    model = DespesaMensal
    template_name = 'despesas_mensais.html'
    context_object_name = 'despesas_mensais'


class HomeListView(ListView):
    model = Despesa
    template_name = 'home.html'
    context_object_name = 'despesas'

    def get_queryset(self):
        queryset = super().get_queryset()
        banco_id = self.request.GET.get('bank')
        mes_id = self.request.GET.get('months')

        if banco_id:
            queryset = queryset.filter(bank_id=banco_id)
        if mes_id:
            queryset = queryset.filter(month_id=mes_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bancos'] = Bank.objects.all()
        context['meses'] = Month.objects.all()

        context['total_despesas'] = context['despesas'].aggregate(Sum('value'))
        ['value__sum'] or 0

        return context


class NovaDespesaView(CreateView):
    model = Despesa
    form_class = DespesaModelForm
    template_name = 'nova_despesa.html'
    success_url = reverse_lazy('home')


class DetalheDespesa(DetailView):
    model = Despesa
    template_name = 'detalhe_despesa.html'


class DeletarDespesaView(DeleteView):
    model = Despesa
    template_name = 'deletar_despesa.html'
    success_url = reverse_lazy('home')
