from django.db import models
from django.contrib.auth.models import User
from django.db.models import F


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    budget = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("name", "user"),)

    def __str__(self):
        return self.name


class Expense(models.Model):
    user = models.ForeignKey(User, related_name="expenses", on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, related_name="categories", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    amount = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.name
