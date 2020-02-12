from django import forms
from .models import Customer, Repair, Ticket



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



