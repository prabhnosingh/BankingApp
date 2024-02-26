from django import forms
from account.models import KYC
from django.forms import ImageField ,FileInput ,DateInput

class DateInput(forms.DateInput):
    input_type = 'date'

class KYCForm(forms.ModelForm):
    identity_image = ImageField(widget=FileInput)

    class Meta:
        model = KYC
        fields=['full_name','image','marrital_status','identity_type','date_of_birth','signature','city','mobile','fax','state','country','gender','identity_image']

    widgets={
        "full_name":forms.TextInput(attrs=
                                    {'placeholder':'Full Name'}
                                    ),
        "mobile": forms.TextInput(attrs=
                                  {'placeholder': 'Mobile'}
                                  ),
        "fax": forms.TextInput(attrs=
                               {'placeholder': 'Fax number'}
                               ),

        "country": forms.TextInput(attrs= {'placeholder': 'Country'}),
        "state": forms.TextInput(attrs={'placeholder': 'State'}),
        "city": forms.TextInput(attrs={'placeholder': 'City'}),
    }
