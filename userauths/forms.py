from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User
# from bankingApp.userauths.models import User  # if you face an error at this line, try changing the import according


# to your file structure

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
