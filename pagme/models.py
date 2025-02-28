from django.db import models
from django.utils.translation import gettext_lazy as _

class Expense(models.Model):
    value = models.PositiveIntegerField(
        verbose_name= _("Valor Devido"),
        null=False,
        blank=False
    )

    days = models.DateField(
        verbose_name= _("Dias em Atraso"),
        null=False,
        blank=False
    )

    def __str__(self):
        return f"{self.value} - {self.days}"
    
    class Meta:
        verbose_name = "Divida"
        verbose_name_plural = "Dividas"