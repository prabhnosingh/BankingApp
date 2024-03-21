from django import forms
from core.models import CreditCard

class CreditCardForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Name on Card"}))
    number = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": "Card Number"}))
    month = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": "Month of Expiry"}))
    year = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": "Year of Expiry"}))
    cvv = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": "CVV"}))

    class Meta:
        model = CreditCard
        fields = ["name", "number", "month", "year", "cvv","card_type"]