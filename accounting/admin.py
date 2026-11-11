from django.contrib import admin
from .models import Business, Transaction

@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "currency", "created_at")
    search_fields = ("name", "owner__username")

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("description", "business", "transaction_type", "amount", "transaction_date")
    list_filter = ("transaction_type", "category", "transaction_date")
    search_fields = ("description", "business__name")
