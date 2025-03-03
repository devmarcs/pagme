# Generated by Django 5.1.4 on 2025-03-03 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagme', '0008_remove_debtors_expanse_debtor'),
    ]

    operations = [
        migrations.AddField(
            model_name='debtors',
            name='last_payment_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data do Último Pagamento'),
        ),
        migrations.AddField(
            model_name='debtors',
            name='value',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='Valor Devido'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Expense',
        ),
    ]
