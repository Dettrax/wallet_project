# wallet_app/forms.py
from django import forms
from .models import User, PhoneNumber, EmailAddress, BankAccount, Transaction

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'date_of_birth']

class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['number', 'is_primary']

class EmailAddressForm(forms.ModelForm):
    class Meta:
        model = EmailAddress
        fields = ['email', 'is_primary']

class BankAccountForm(forms.ModelForm):
    class Meta:
        model = BankAccount
        fields = ['account_number', 'routing_number', 'bank_name', 'is_primary']

class TransactionSearchForm(forms.Form):
    query = forms.CharField(required=False)
    date_from = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    TRANSACTION_TYPES = [('', 'All')] + list(Transaction.TRANSACTION_TYPES)
    transaction_type = forms.ChoiceField(choices=TRANSACTION_TYPES, required=False)