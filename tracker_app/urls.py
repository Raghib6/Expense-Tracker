from django.urls import path
from . import views

urlpatterns = [
    path("homepage/", views.home, name="homepage"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("set-budget/", views.set_budget, name="set_budget"),
    path("update-budget/<str:id>/", views.update_budget, name="update_budget"),
    path("add-expense/", views.add_expense, name="add_expense"),
    path("budget-summary/", views.budget_summary, name="budget_summary"),
    path(
        "categorywise_expenses/<str:id>/",
        views.categorywise_expenses,
        name="categorywise_expenses",
    ),
]
