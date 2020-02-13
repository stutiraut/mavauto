from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm

now = timezone.now()
def home(request):
   return render(request, 'crm/home.html',
                 {'crm': home})

@login_required
def customer_list(request):
    customer = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/customer_list.html',
                 {'customers': customer})

@login_required
def customer_edit(request, pk):
   customer = get_object_or_404(Customer, pk=pk)
   if request.method == "POST":
       # update
       form = CustomerForm(request.POST, instance=customer)
       if form.is_valid():
           customer = form.save(commit=False)
           customer.updated_date = timezone.now()
           customer.save()
           customer = Customer.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/customer_list.html',
                         {'customers': customer})
   else:
        # edit
       form = CustomerForm(instance=customer)
   return render(request, 'crm/customer_edit.html', {'form': form})


@login_required
def customer_new(request):
   if request.method == "POST":
       form = CustomerForm(request.POST)
       if form.is_valid():
           customer = form.save(commit=False)
           customer.created_date = timezone.now()
           customer.save()
           customer = Customer.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/customer_list.html',
                         {'customers': customer})

   else:
       form = CustomerForm()
   return render(request, 'crm/customer_new.html', {'form': form})

@login_required
def customer_delete(request, pk):
   customer = get_object_or_404(Customer, pk=pk)
   customer.delete()
   return redirect('crm:customer_list')



@login_required
def repair_list(request):
    repair = Repair.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/repair_list.html',
                 {'repairs': repair})


@login_required
def repair_edit(request, pk):
   repair = get_object_or_404(Repair, pk=pk)
   if request.method == "POST":
       form = RepairForm(request.POST, instance=repair)
       if form.is_valid():
           repair = form.save()
           # stock.customer = stock.id
           repair.updated_date = timezone.now()
           repair.save()
           repairs = Repair.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/repair_list.html', {'repairs': repairs})
   else:
       # print("else")
       form = RepairForm(instance=repair)
   return render(request, 'crm/repair_edit.html', {'form': form})

@login_required
def repair_delete(request, pk):
    repair = get_object_or_404(Repair, pk=pk)
    repair.delete()
    return redirect('crm:repair_list')

@login_required
def repair_new(request):
   if request.method == "POST":
       form = RepairForm(request.POST)
       if form.is_valid():
           repair = form.save(commit=False)
           repair.created_date = timezone.now()
           repair.save()
           repairs = Repair.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/repair_list.html',
                         {'repairs': repairs})

   else:
       form = RepairForm()
       # print("Else")
   return render(request, 'crm/repair_new.html', {'form': form})


@login_required
def ticket_list(request):
    ticket = Ticket.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/ticket_list.html',
                 {'tickets': ticket})


@login_required
def ticket_delete(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.delete()
    return redirect('crm:ticket_list')


@login_required
def ticket_edit(request, pk):
   ticket = get_object_or_404(Ticket, pk=pk)
   if request.method == "POST":
       # update
       form = TicketForm(request.POST, instance=ticket)
       if form.is_valid():
           ticket = form.save(commit=False)
           ticket.updated_date = timezone.now()
           ticket.save()
           ticket = Ticket.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/ticket_list.html',
                         {'tickets': ticket})
   else:
        # edit
       form = TicketForm(instance=ticket)
   return render(request, 'crm/ticket_edit.html', {'form': form})


@login_required
def ticket_new(request):
   if request.method == "POST":
       form = TicketForm(request.POST)
       if form.is_valid():
           ticket = form.save(commit=False)
           ticket.created_date = timezone.now()
           ticket.save()
           tickets = Ticket.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/ticket_list.html',
                         {'tickets': tickets})

   else:
       form = TicketForm()
       # print("Else")
   return render(request, 'crm/ticket_new.html', {'form': form})



def store_location(request):
    return render(request, 'map/storelocation.html',
                 {'map': store_location})

