from django.shortcuts import render, redirect
from account.models import KYC, Account
from core.models import Transaction
from account.forms import KYCForm
from django.contrib import messages
from core.forms import CreditCardForm
from core.models import CreditCard

#  Display the Account Details of the User in account.html template:
def account(request):
    if request.user.is_authenticated:
        try:
            kyc = KYC.objects.get(user=request.user)
        except:
            messages.warning(request, "You need to submit your kyc")
            return redirect("account:kyc-reg")

        account = Account.objects.get(user=request.user)
    else:
        messages.warning(request, "You need to login to access the dashboard")
        return redirect("userauths:sign-in")

    context = {
        "kyc": kyc,
        "account": account,
    }
    return render(request, "account/account.html", context)



def kyc_registration(request):
    user = request.user
    account = Account.objects.get(user=user)

    try:
        kyc = KYC.objects.get(user=user)
    except:
        kyc = None

    if request.method == "POST":
        form = KYCForm(request.POST, request.FILES, instance=kyc)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = user
            new_form.account = account
            new_form.save()
            messages.success(request, "KYC Form submitted successfully, In review now.")
            return redirect("account:account")
    else:
        form = KYCForm(instance=kyc)
    context = {
        "account": account,
        "form": form,
        "kyc": kyc,
    }
    return render(request, "account/kyc-form.html", context)

#def dashboard(request):

   # return render(request, "account/dashboard.html")
def dashboard(request):
    if request.user.is_authenticated:
        try:
            kyc = KYC.objects.get(user=request.user)
        except:
            messages.warning(request, "You need to submit your kyc")
            return redirect("account:kyc-reg")

        recent_transfer = Transaction.objects.filter(sender=request.user, transaction_type="transfer",
                                                     status="completed").order_by("-id")[:1]
        recent_recieved_transfer = Transaction.objects.filter(reciever=request.user,
                                                              transaction_type="transfer").order_by("-id")[:1]

        sender_transaction = Transaction.objects.filter(sender=request.user, transaction_type="transfer").order_by(
            "-id")
        reciever_transaction = Transaction.objects.filter(reciever=request.user, transaction_type="transfer").order_by(
            "-id")

        request_sender_transaction = Transaction.objects.filter(sender=request.user, transaction_type="request")
        request_reciever_transaction = Transaction.objects.filter(reciever=request.user, transaction_type="request")

        account = Account.objects.get(user=request.user)
        credit_card = CreditCard.objects.filter(user=request.user)

        if request.method =="POST":
            form = CreditCardForm(request.POST)
            if form.is_valid():
                new_form = form.save(commit=False)
                new_form.user = request.user
                new_form.save()

                card_is = new_form.card_id
                messages.success(request, "Card Details Submitted Successfully")
                return redirect("account:dashboard")
        else:
            form = CreditCardForm()
    else:
        messages.warning(request, "You need to login to access the dashboard")
        return redirect("userauths:sign-in")

    context = {
        "kyc": kyc,
        "account": account,
        "sender_transaction": sender_transaction,
        "reciever_transaction": reciever_transaction,
        'form': form,
        "credit_card": credit_card,

        'request_sender_transaction': request_sender_transaction,
        'request_reciever_transaction': request_reciever_transaction,
        'recent_transfer': recent_transfer,
        'recent_recieved_transfer': recent_recieved_transfer,
    }
    return render(request, "account/dashboard.html", context)
