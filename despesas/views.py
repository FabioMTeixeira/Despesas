from django.shortcuts import redirect, render
from despesas.forms import DespesaModelForm
from .models import Despesa

# Create your views here.


def home_view(request):
    despesas = Despesa.objects.all()
    search = request.GET.get('search')

    if search:
        despesas = despesas.filter(name__icontains=search)
    return render(request, 'home.html', {'despesas': despesas})


def nova_despesa_view(request):
    if request.method == 'POST':
        nova_despesa_form = DespesaModelForm(request.POST)
        if nova_despesa_form.is_valid():
            nova_despesa_form.save()
            return redirect('home')
    else:
        nova_despesa_form = DespesaModelForm()
    return render(request, 'nova_despesa.html', {'nova_despesa_form': nova_despesa_form})
