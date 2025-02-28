from django.contrib import admin
from .models import Expense


class ExpanseAdmin(admin.ModelAdmin):
    list_display = [
        "value",
        "days",
    ]

admin.site.register(Expense, ExpanseAdmin)