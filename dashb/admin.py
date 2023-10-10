# dashb/admin.py

from django.contrib import admin
from .models import Trader, Trade


@admin.register(Trader)
class TraderAdmin(admin.ModelAdmin):
    list_display = ('name', 'starting_capital')  # Display the current capital instead of 'balance'
    search_fields = ('name',)
    list_filter = ('name',)

      # Set a custom column header

@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ('trader', 'timestamp', 'profit_or_loss')
    list_filter = ('timestamp', 'trader__name')
    date_hierarchy = 'timestamp'
