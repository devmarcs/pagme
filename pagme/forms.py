from django import forms
from pagme.models import Expense, Debtors

class DebtorsExpenseForm(forms.ModelForm):
    value = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        label="Valor devido"
    )
    last_payment_date = forms.DateField(
        widget=forms.SelectDateWidget(),
        label="Data do último pagamento"
    )

    class Meta:
        model = Debtors
        fields = [
            "name",
            "nickname",
        ]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o nome do devedor",
                }
            ),
            "nickname": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o apelido do devedor",
                }
            ),
        }

    def save(self, commit=True):
        
        debtor = super().save(commit=False)
        debtor.save()
        
        Expense.objects.create(
            value=self.cleaned_data["value"],
            days=self.cleaned_data["last_payment_date"],
            debtor=debtor
        )

        return debtor