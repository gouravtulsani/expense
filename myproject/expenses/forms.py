from django import forms
from django.contrib.auth.models import User

from .models import Expenses



class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expenses
        fields = ['name','number','company','email','image','is_favorite']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


