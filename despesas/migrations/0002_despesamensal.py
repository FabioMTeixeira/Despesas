# Generated by Django 5.0.6 on 2024-06-18 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('despesas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DespesaMensal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.IntegerField()),
                ('valor_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
            options={
                'unique_together': {('mes',)},
            },
        ),
    ]
