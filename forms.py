from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Business, Transaction

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ("name", "address", "currency")
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "e.g. My Shop"}),
            "address": forms.TextInput(attrs={"placeholder": "Business address (optional)"}),
            "currency": forms.Select(choices=[("INR", "INR — Indian Rupee"), ("USD", "USD — US Dollar"), ("AED", "AED — UAE Dirham")]),
        }

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ("description", "category", "transaction_type", "amount", "transaction_date")
        widgets = {
            "description": forms.TextInput(attrs={"placeholder": "e.g. Product sale"}),
            "category": forms.TextInput(attrs={"placeholder": "e.g. Sales, Rent, Travel"}),
            "transaction_date": forms.DateInput(attrs={"type": "date"}),
            "amount": forms.NumberInput(attrs={"min": "0.01", "step": "0.01", "placeholder": "0.00"}),
        }
