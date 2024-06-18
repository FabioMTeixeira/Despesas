from django.db import models

# Create your models here.


class Bank(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Month(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class DespesaMensal(models.Model):
    mes = models.IntegerField()
    valor_total = models.FloatField()

    class Meta:
        unique_together = ('mes',)


class Despesa(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    value = models.FloatField(blank=False, null=False)
    date = models.DateField(auto_now_add=True)
    bank = models.ForeignKey(
        Bank, on_delete=models.PROTECT, related_name="des_bank")
    month = models.ForeignKey(
        Month, on_delete=models.PROTECT, related_name="des_month")
    description = models.TextField(blank=False, null=False)

    def __str__(self):
        return f'Essa despesa é do {self.name} do bank {self.bank}'
