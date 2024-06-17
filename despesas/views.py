from despesas.forms import DespesaModelForm
from .models import Despesa, Bank
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


class HomeListView(ListView):
    model = Despesa
    template_name = 'home.html'
    context_object_name = 'despesas'

    def get_queryset(self):
        queryset = super().get_queryset()
        banco_id = self.request.GET.get('bank')
        if banco_id:
            queryset = queryset.filter(bank_id=banco_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bancos'] = Bank.objects.all()
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
