from django.db import models

class App_users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    # class Meta:
    #     db_table = 'app_users'