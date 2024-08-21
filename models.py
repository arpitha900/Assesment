from django.db import models
from django.contrib.auth.models import User



class Stock(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user} - {self.stock} - {self.transaction_type}"

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.stock}"

class Alert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    price_target = models.DecimalField(max_digits=10, decimal_places=2)
    email_sent = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.stock} - {self.price_target}"
