from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from pagme.models import Expense
from pagme.forms import DebtorsExpenseForm
from django.urls import reverse_lazy
from django.contrib import messages


class ListPeoplesExpenseViews(ListView):
    model = Expense
    template_name = "template/expense/list_peoples.html"
    context_object_name = "expenses"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["expenses"] = Expense.objects.all() 
        return context
    

class CreateDebtorView(FormView):
    template_name = "template/expense/create_debtor.html"
    form_class = DebtorsExpenseForm
    success_url = reverse_lazy("pagme:peoples")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Devedor e dívida cadastrados com sucesso!")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Erro ao cadastrar o devedor!")
        print(f"Deu erro irmão {form.errors}")
        response = super().form_invalid(form)
        return response
    


list_people = ListPeoplesExpenseViews.as_view()
create = CreateDebtorView.as_view()
