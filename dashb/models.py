from django.db import models
from . import db_connection
from decimal import Decimal
from django.contrib.auth.models import User
from django.db.models import Sum 


dashb_connections = db_connection.db['ft9ja']

class Trader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    starting_capital = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('100.00'))

    def __str__(self):
        return f'{self.name}'    


class Trade(models.Model):
    trader = models.ForeignKey(Trader, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    profit_or_loss = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f'{self.trader}: {self.profit_or_loss} as at {self.timestamp}'