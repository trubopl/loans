from django.db import models


class CompaniesLoans(models.Model):
    name = models.CharField(max_length=100)
    min_amount = models.IntegerField()
    max_amount = models.IntegerField()
    min_days = models.IntegerField()
    max_days = models.IntegerField()
    first_free = models.BooleanField()
    amount_first_free = models.IntegerField()
    installment_loan = models.BooleanField()
    installment_min_amount = models.IntegerField()
    installment_max_amount = models.IntegerField()
    installment_min_days = models.IntegerField()
    installment_max_days = models.IntegerField()
    miscs = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name


class CompaniesCredit(models.Model):
    name = models.CharField(max_length=100)
    min_amount = models.IntegerField()
    max_amount = models.IntegerField()
    min_days = models.IntegerField()
    max_days = models.IntegerField()
    miscs = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name
