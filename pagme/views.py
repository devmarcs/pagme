from django.shortcuts import render
from django.views.generic import ListView
from .models import Expense


class ListPeoplesExpenseViews(ListView):
    model = Expense
    template_name = "template/expense/list_peoples.html"
    context_object_name = "expenses"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["Expenses"] = Expense.objects.all()
        return context

list_people = ListPeoplesExpenseViews.as_view()
