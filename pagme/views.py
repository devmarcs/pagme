from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView, UpdateView
from pagme.models import Expense, Debtors
from pagme.forms import DebtorsExpenseForm, DebtorsExpenseUpdateForm
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
        response = super().form_invalid(form)
        return response
    
class UpdateDebtor(UpdateView):
    template_name = "template/expense/update_debtor.html"
    model = Debtors
    form_class = DebtorsExpenseUpdateForm
    success_url = reverse_lazy("pagme:peoples")

    def get_object(self, queryset=None):
        return super().get_object(queryset)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        # Preenche os campos do formulário com os dados da despesa associada
        expense = Expense.objects.filter(debtor=self.object).first()
        if expense:
            form.initial['value'] = expense.value
            form.initial['last_payment_date'] = expense.days
        return form

    def form_valid(self, form):
        # Salva o devedor
        debtor = form.save(commit=False)
        debtor.save()

        # Atualiza ou cria a despesa associada
        Expense.objects.update_or_create(
            debtor=debtor,
            defaults={
                'value': form.cleaned_data['value'],
                'days': form.cleaned_data['last_payment_date'],
            }
        )
        messages.success(self.request, "Devedor e dívida atualizados com sucesso!")
        return super().form_valid(form)  
    
    def form_invalid(self, form):
        messages.error(self.request, "Erro ao atualizar o devedor!")
        return super().form_invalid(form)


list_people = ListPeoplesExpenseViews.as_view()
create = CreateDebtorView.as_view()
update = UpdateDebtor.as_view()
