from django.db import models
from django.contrib.auth.models import User

class App_users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=2)



class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
