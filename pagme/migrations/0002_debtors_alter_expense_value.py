# Generated by Django 5.1.4 on 2025-03-02 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagme', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debtors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('nickname', models.CharField(max_length=200, verbose_name='Apelido')),
            ],
            options={
                'verbose_name': 'Devedor',
                'verbose_name_plural': 'Devedores',
            },
        ),
        migrations.AlterField(
            model_name='expense',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=2, verbose_name='Valor Devido'),
        ),
    ]
