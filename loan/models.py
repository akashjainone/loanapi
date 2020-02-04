from django.db import models
import datetime
from django.conf import settings


class Loan(models.Model):
    name = models.CharField(max_length=60, unique=False)
    phone = models.IntegerField(primary_key=True, unique=True)
    amount = models.IntegerField()
    rate = models.IntegerField()
    days = models.IntegerField()
    created_date = models.DateTimeField(default=datetime.datetime.now, blank=False)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def non_approved(self):
        # Count all non approved loans
        return Loan.objects.filter(loan=self, approved=0)

    def complete_tasks(self):
        # Count all approved loans
        return Loan.objects.filter(loan=self, approved=1)

    class Meta:
        ordering = ["name"]
