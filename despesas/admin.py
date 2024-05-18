from django.contrib import admin
from .models import Despesa, Bank, Month

# Register your models here.


class DespesaAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'date', 'bank', 'month', 'description')
    search_fields = ('name',)


class BankAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)


class MonthAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name',)


admin.site.register(Despesa, DespesaAdmin)
admin.site.register(Bank, BankAdmin)
admin.site.register(Month, MonthAdmin)
