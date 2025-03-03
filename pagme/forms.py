# from django import forms
# from pagme.models import Debtors

# forms.py
from django import forms
from pagme.models import Debtors

class DebtorsForm(forms.ModelForm):
    class Meta:
        model = Debtors
        fields = [
            "name",
            "nickname",
            "value",
            "last_payment_date",
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
            "value": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o valor devido",
                    "step": 0.01,
                }
            ),
            "last_payment_date": forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
        }
    
# # Formulário de Edição

# class DebtorsExpenseUpdateForm(forms.ModelForm):
#     value = forms.DecimalField(
#         max_digits=10,
#         decimal_places=2,
#         label="Valor Devido",
#         widget=forms.NumberInput(
#             attrs={
#                 "class": "form-control",
#                 "placeholder": "Digite o valor devido",
#                 "step": 0.01,
#             }
#         )
#     )
#     last_payment_date = forms.DateField(
#         widget=forms.DateInput(
#             format=('%Y-%m-%d'),
#             attrs={
#                 "class": "form-control",
#                 "type": "date",
#             }
#         ),
#         label="Data do Último Pagamento"
#     )

#     class Meta:
#         model = Debtors
#         fields = [
#             "name",
#             "nickname",
#             "value",  # Campo do modelo Expense
#             "last_payment_date",  # Campo do modelo Expense
#         ]
#         widgets = {
#             "name": forms.TextInput(
#                 attrs={
#                     "class": "form-control",
#                     "placeholder": "Digite o nome do devedor",
#                 }
#             ),
#             "nickname": forms.TextInput(
#                 attrs={
#                     "class": "form-control",
#                     "placeholder": "Digite o apelido do devedor",
#                 }
#             ),
#         }