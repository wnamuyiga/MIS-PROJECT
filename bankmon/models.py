from django.db import models

# Create your models here.

# for bank details
class Bank(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField()
    email = models.EmailField()

    def __str__(self):
        return self.name


# for branch details
class Branch(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    contant_person = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    email = models.EmailField()
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='branch')

    def __str__(self):
        return self.name


# Service provider details
class Provider(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    SERVICE_CHOICES = (
        ('Mobile Money', 'Mobile Money'),
        ('Airtime', 'Airtime'),
    )
    service = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    contant_person = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    website = models.URLField()
    email = models.EmailField()

    def __str__(self):
        return self.name

# Transaction details
class Transaction(models.Model):
    name = models.CharField(max_length=200)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='transaction')
    STATUS_CHOICES = (
        ('Success', 'Success'),
        ('Pending', 'Pending'),
        ('Failed', 'Failed'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name



class Problem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='problem', blank=True, null=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name='problem', blank=True, null=True)
    attention = models.CharField(max_length=30)
    CATEGORY_CHOICES = (
        ('failures', 'failures'),
        ('warnings', 'warnings'),
        ('anomalies', 'anomalies'),
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    STATUS_CHOICES = (
        ('solved', 'solved'),
        ('Pending', 'Pending'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name





