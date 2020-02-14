from django import forms
from .models import Customer, Repair, Ticket
from django.contrib.auth.models import User


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cust_number', 'cust_name', 'address', 'city', 'state', 'zipcode', 'email', 'phone_number',)


class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = ('cust_name', 'repair_id', 'repair_item', 'repair_model', 'description', 'repair_charge',)


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('cust_name', 'repair_id', 'setup_time', 'Issue', 'severity',)



class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
