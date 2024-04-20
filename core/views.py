from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.db import IntegrityError

from account.models import Account
from core.forms import SupportCaseForm, ContactForm
from .models import Contact


# Create your views here.

def index(request):
    return render(request,"core/index.html")

def about_us(request):
    return render(request,"core/aboutus.html")

def contact(request):
    return render(request,"core/contact.html")

def support_page(request):
    if request.method == 'POST':
        print("I am not ")
        form = SupportCaseForm(request.POST)
        if form.is_valid():
            account_number = request.POST.get('account')
            account_id = request.POST.get('account_id')

            try:
                account = Account.objects.get(account_number=account_number, account_id=account_id)
            except Account.DoesNotExist:
                messages.warning(request, "Invalid Account Number or Account ID.")
                return redirect('account:account')

            support_case = form.save(commit=False)
            support_case.account = account
            support_case.save()
            messages.success(request, "Support case submitted successfully. Your Case ID is: {}".format(support_case.id))
            return redirect('account:account')

    else:
        # Fetching account details from the logged-in user or session
        if request.user.is_authenticated:
            account = Account.objects.get(user=request.user)
            print("i am authenticated")
        else:
            account = None

        form = SupportCaseForm(account=account)

    return render(request, 'core/support_page.html', {'form': form})

@login_required
def save_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                account_number = form.cleaned_data["account_number"]
                account = Account.objects.filter(account_number=account_number).first()
                if account:
                    contact = form.save(commit=False)
                    contact.user = request.user
                    print(contact.user)
                    contact.save()
                    return redirect("core:contact_list")  # Redirect to contact list view
                else:
                    form.add_error("account_number", "Account number not found.")
            except IntegrityError:
                form.add_error(None, "A contact with the same name or account number already exists for this user.")
    else:
        form = ContactForm()
    return render(request, "core/contact_form.html", {"form": form})

def contact_list(request):
    contacts = Contact.objects.filter(user=request.user)
    return render(request, "core/contact_list.html", {"contacts": contacts})
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete_contact()
    return redirect('core:contact_list')