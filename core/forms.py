from django import forms
from core.models import CreditCard, SupportCase


class CreditCardForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Name on Card"}))
    number = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": "Card Number"}))
    month = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": "Month of Expiry"}))
    year = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": "Year of Expiry"}))
    cvv = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": "CVV"}))

    class Meta:
        model = CreditCard
        fields = ["name", "number", "month", "year", "cvv","card_type"]

class SupportCaseForm(forms.ModelForm):
    class Meta:
        model = SupportCase
        fields = ['name', 'contact_number', 'email', 'message']
        labels = {
            'name': 'Name',
            'contact_number': 'Contact Number',
            'email': 'Email',
            'message': 'Message'
        }

    def __init__(self, *args, **kwargs):
        # Fetch Account Number and Account ID
        account = kwargs.pop('account', None)
        super().__init__(*args, **kwargs)
        if account:
            self.fields['account'] = forms.CharField(initial=account.account_number, widget=forms.HiddenInput())
            self.fields['account_id'] = forms.CharField(initial=account.account_id, widget=forms.HiddenInput())
