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
    
