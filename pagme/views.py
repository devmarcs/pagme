from django.utils import timezone
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from pagme.models import Debtors
from pagme.forms import DebtorsForm
from django.contrib import messages

class CreateDebtorView(CreateView):
    template_name = "template/expense/create_and_edit_debtor.html"
    model = Debtors
    form_class = DebtorsForm
    success_url = reverse_lazy("pagme:list_debtors")

    def form_valid(self, form):
        messages.success(self.request, "Devedor cadastrado com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Erro ao cadastrar o devedor!")
        return super().form_invalid(form)
    
class ListDebtors(ListView):
    model = Debtors
    template_name = "template/expense/list_debtors.html"
    context_object_name = "expenses"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        today = timezone.now().date()
        
        for debtor in context["expenses"]:
            if debtor.last_payment_date:
                days_late = (today - debtor.last_payment_date).days
                debtor.days_late = days_late
            else:
                debtor.days_late = None
        return context
    

class UpdateDebtor(UpdateView):
    template_name = "template/expense/create_and_edit_debtor.html"
    model = Debtors
    form_class = DebtorsForm
    success_url = reverse_lazy("pagme:list_debtors")

    def form_valid(self, form):
        messages.success(self.request, "Devedor atualizado com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Erro ao atualizar o devedor!")
        return super().form_invalid(form)
    
class DeleteDebtor(DeleteView):
    model = Debtors
    template_name = "template/expense/delete_debtors.html"
    success_url = reverse_lazy("pagme:list_debtors")
    context_object_name = "debtors"

    def delete(self, request, *args, **kwargs):
        
        self.object = self.get_object()
        self.object.delete()
        messages.success(self.request, "Devedor exclúido com sucesso!")
        return super().delete(request, *args, **kwargs)


list = ListDebtors.as_view()
create = CreateDebtorView.as_view()
update = UpdateDebtor.as_view()
delete = DeleteDebtor.as_view()
