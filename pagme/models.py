from django.db import models
from django.utils.translation import gettext_lazy as _

class Debtors(models.Model):
    name = models.CharField(
        verbose_name=_("Nome"),
        max_length=200,
        null=False,
        blank=False,
    )

    nickname = models.CharField(
        verbose_name=_("Apelido"),
        max_length=200,
        null=True,
        blank=True
    )

    value = models.DecimalField(
        verbose_name=_("Valor Devido"),
        decimal_places=2,
        max_digits=10,
        null=False,
        blank=False
    )

    last_payment_date = models.DateField(
        verbose_name=_("Data do Último Pagamento"),
        null=True,
        blank=True
    )

    is_paid = models.BooleanField(
        verbose_name= _("Está pago?"),
        default=False,
        null=False,
        blank=False
    )

    def __str__(self):
        return f"{self.name} - {self.nickname}"

    class Meta:
        verbose_name = "Devedor"
        verbose_name_plural = "Devedores"