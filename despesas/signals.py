from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Despesa, DespesaMensal


@receiver(post_save, sender=Despesa)
def atualizar_despesa_mensal(sender, instance, created, **kwargs):
    if created:
        mes = instance.date.month
        despesa_mensal, _ = DespesaMensal.objects.get_or_create(
            mes=mes)
        despesa_mensal.valor_total += instance.value
        despesa_mensal.save()
