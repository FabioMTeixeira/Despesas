# Generated by Django 5.0.6 on 2024-05-14 21:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='des_bank', to='despesas.bank')),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='des_month', to='despesas.month')),
            ],
        ),
    ]