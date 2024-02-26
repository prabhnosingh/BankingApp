from django import forms
from account.models import KYC
from django.forms import ImageField ,FileInput ,DateInput

class DateInput(forms.DateInput):
    input_type = 'date'

class KYCForm(forms.ModelForm):
    identity_image = ImageField(widget=FileInput)