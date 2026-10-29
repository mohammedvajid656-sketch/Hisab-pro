from decimal import Decimal
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .forms import SignUpForm, BusinessForm, TransactionForm
from .models import Business, Transaction

def signup(request):
    if request.user.is_authenticated:
        return redirect("home")
    form = SignUpForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Account created. Create your first business to begin.")
        return redirect("business_create")
    return render(request, "registration/signup.html", {"form": form})

@login_required
def home(request):
    businesses = Business.objects.filter(owner=request.user)
    selected_id = request.session.get("active_business_id")
    business = businesses.filter(id=selected_id).first() if selected_id else businesses.first()
    if not business:
        return redirect("business_create")
    request.session["active_business_id"] = business.id
    return redirect("dashboard", business_id=business.id)

@login_required
def business_create(request):
    form = BusinessForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        business = form.save(commit=False)
        business.owner = request.user
        business.save()
        request.session["active_business_id"] = business.id
        messages.success(request, "Business created successfully.")
        return redirect("dashboard", business_id=business.id)
    return render(request, "accounting/business_form.html", {"form": form})

@login_required
def dashboard(request, business_id):
    business = get_object_or_404(Business, id=business_id, owner=request.user)
    request.session["active_business_id"] = business.id
    transactions = Transaction.objects.filter(business=business)
    income = transactions.filter(transaction_type=Transaction.INCOME).aggregate(total=Sum("amount"))["total"] or Decimal("0.00")
    expenses = transactions.filter(transaction_type=Transaction.EXPENSE).aggregate(total=Sum("amount"))["total"] or Decimal("0.00")
    context = {
        "business": business,
        "businesses": Business.objects.filter(owner=request.user),
        "income": income,
        "expenses": expenses,
        "balance": income - expenses,
        "transaction_count": transactions.count(),
        "recent_transactions": transactions[:8],
    }
    return render(request, "accounting/dashboard.html", context)

@login_required
def transaction_create(request, business_id):
    business = get_object_or_404(Business, id=business_id, owner=request.user)
    form = TransactionForm(request.POST or None, initial={"transaction_date": timezone.localdate()})
    if request.method == "POST" and form.is_valid():
        transaction = form.save(commit=False)
        transaction.business = business
        transaction.save()
        messages.success(request, "Transaction saved successfully.")
        return redirect("dashboard", business_id=business.id)
    return render(request, "accounting/transaction_form.html", {"form": form, "business": business})

@login_required
def transaction_list(request, business_id):
    business = get_object_or_404(Business, id=business_id, owner=request.user)
    transactions = Transaction.objects.filter(business=business)
    return render(request, "accounting/transactions.html", {
        "business": business, "businesses": Business.objects.filter(owner=request.user),
        "transactions": transactions,
    })

@login_required
def language_switch(request, language):
    if language not in ("en", "ml"):
        language = "en"
    request.session["hisabpro_language"] = language
    response = redirect(request.META.get("HTTP_REFERER") or "home")
    response.set_cookie("django_language", language, max_age=60 * 60 * 24 * 365)
    return response
