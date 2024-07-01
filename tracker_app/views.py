from django.shortcuts import render, redirect
from django.db.models import Sum
from django.contrib import messages, auth
from django.core.paginator import Paginator
from .decorators import unauthenticated_user
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Category, Expense
from .forms import CategoryForm, ExpenseForm, UserSignUpForm
from .filters import ExpenseFilter


@login_required(login_url="login")
def home(request):
    user = request.user
    if user:
        filter = ExpenseFilter(
            request.GET, request=request, queryset=Expense.objects.filter(user=user)
        )
        paginator = Paginator(filter.qs, 5)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context = {"filter": filter, "expenses": page_obj}
        return render(request, "index.html", context)


@login_required(login_url="login")
def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        category = request.POST["category"]
        amount = request.POST["amount"]
        total = 0
        expense = Expense.objects.filter(category=category)
        if expense.exists():
            previous_total = expense.aggregate(Sum("amount"))["amount__sum"] or 0
            total = int(previous_total) + int(amount)
            category = Category.objects.get(id=category)
            if total > category.budget:
                messages.warning(
                    request,
                    f"The total expense amount {total}Tk exceeds the {category.name}'s budget {category.budget}tk",
                )

        if form.is_valid():
            user = request.user
            name = form.cleaned_data["name"]
            category = form.cleaned_data["category"]
            amount = form.cleaned_data["amount"]
            date = form.cleaned_data["date"]

            expense = Expense.objects.create(
                user=user, name=name, category=category, amount=amount, date=date
            )
            expense.save()
            return redirect("/homepage")
    else:
        form = ExpenseForm()

    context = {
        "form": form,
    }
    return render(request, "add_expenses.html", context)


@login_required(login_url="login")
def set_budget(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = Category.objects.create(
                user=request.user,
                name=form.cleaned_data["name"],
                budget=form.cleaned_data["budget"],
            )
            category.save()
            return redirect("/budget-summary")
    context = {"form": form}
    return render(request, "set_budget.html", context)


@login_required(login_url="login")
def update_budget(request, id):
    order = Category.objects.get(id=id)
    form = CategoryForm(instance=order)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("/budget-summary")
    context = {"form": form}

    return render(request, "set_budget.html", context)


@login_required(login_url="login")
def budget_summary(request):
    user = request.user
    categories = Category.objects.filter(user=user)
    summaries = []
    for category in categories:
        total_expense = (
            Expense.objects.filter(user=user, category=category.id).aggregate(
                Sum("amount")
            )["amount__sum"]
            or 0
        )
        amount_left = category.budget - total_expense
        summaries.append(
            {
                "id": category.id,
                "name": category.name,
                "budget": category.budget,
                "total_expense": total_expense,
                "amount_left": amount_left,
            }
        )
    context = {"summaries": summaries}

    return render(request, "budget_summary.html", context)


@login_required(login_url="login")
def categorywise_expenses(request, id):
    category = Category.objects.get(id=id)
    expenses = Expense.objects.filter(category=category)
    paginator = Paginator(expenses, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"expenses": page_obj}
    return render(request, "expense_list.html", context)


@unauthenticated_user
def signup(request):
    form = UserSignUpForm()
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Congratulations! Your account creation is successfull"
            )
            return redirect("login")
    return render(request, "signup.html", {"form": form})


@unauthenticated_user
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password1"]
        user = authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect("/homepage/")
        else:
            messages.error(request, "Invalid Login credential")
            return redirect("login")
    return render(request, "login.html")


@login_required(login_url="login")
def logout(request):
    auth.logout(request)
    return redirect("login")
