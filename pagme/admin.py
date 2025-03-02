from django.contrib import admin
from .models import Expense, Debtors


class ExpanseAdmin(admin.ModelAdmin):
    list_display = [
        "value",
        "days",
        "debtor",
    ]

class DebitorsAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "nickname",
    ]

admin.site.register(Expense, ExpanseAdmin)
admin.site.register(Debtors, DebitorsAdmin)