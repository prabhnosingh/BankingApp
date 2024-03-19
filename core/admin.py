from django.contrib import admin
from core.models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_editable = ['amount', 'status', 'transaction_type', 'reciever', 'sender']
    list_display = ['user', 'amount', 'status', 'transaction_type', 'reciever', 'sender']

# Register your models here.
admin.site.register(Transaction, TransactionAdmin)