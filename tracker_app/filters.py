import django_filters
from .models import Expense, Category
from django import forms


def categories(request):
    if request is None:
        return Category.objects.none()

    user = request.user
    return Category.objects.filter(user=user)


class ExpenseFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(
        queryset=categories,
        empty_label="Choose....",
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    date = django_filters.DateFromToRangeFilter(
        widget=django_filters.widgets.RangeWidget(
            attrs={
                "placeholder": "YYYY/MM/DD",
            }
        )
    )

    class Meta:
        model = Expense
        fields = ["category", "date"]
