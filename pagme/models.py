from django.db import models
from django.utils.translation import gettext_lazy as _


class Expense(models.Model):
    value = models.DecimalField(
        verbose_name= _("Valor Devido"),
        decimal_places=2,
        max_digits=10,
        null=False,
        blank=False
    )

    days = models.DateField(
        verbose_name= _("Dias em Atraso"),
        null=False,
        blank=False
    )

    debtor = models.ForeignKey( 
        'Debtors',
        on_delete=models.CASCADE,
        related_name='expenses',
        verbose_name=_("Devedor"),
        null=False,
        blank=False
    )

    def __str__(self):
        return f"{self.value} - {self.days}"
    
    class Meta:
        verbose_name = "Divida"
        verbose_name_plural = "Dividas"

class Debtors(models.Model):
    name = models.CharField(
        verbose_name= _("Nome"),
        max_length=200,
        null=False,
        blank=False,
    )

    nickname = models.CharField(
        verbose_name= _("Apelido"),
        max_length=200,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.name} - {self.nickname}"
    
    class Meta:
        verbose_name = "Devedor"
        verbose_name_plural = "Devedores"