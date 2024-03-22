from django.shortcuts import render, redirect
from account.models import KYC, Account
from core.models import Transaction
from account.forms import KYCForm
from django.contrib import messages
from core.forms import CreditCardForm
from core.models import CreditCard


def card_detail(request, card_id):
    account = Account.objects.get(user=request.user)
    credic_card = CreditCard.objects.get(card_id=card_id, user=request.user)

    context = {
        "account": account,
        "credic_card": credic_card,
    }
    return render(request, "credit_card/card-detail.html", context)
