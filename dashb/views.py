import random
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import transaction
from django.contrib.auth import login, logout
import matplotlib.pyplot as plt
import io
import base64
from dashb.models import Trader, Trade
from django.http import JsonResponse
from decimal import Decimal

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'dashb/register.html')
    
    current_trader = Trader.objects.get(user_id=request.user)
    capital = current_trader.starting_capital

    # Simulate a new profit or loss based on the trader's capital
    new_profit_or_loss = simulate_profit_or_loss(capital)

    # Get the existing trades for the trader
    trades = current_trader.trade_set.all()

    # Calculate the new profit or loss based on the previous trades
    if trades:
        previous_profit_or_loss = trades.latest('timestamp').profit_or_loss
        new_profit_or_loss += float(previous_profit_or_loss)

    # Create a new trade with the simulated profit or loss
    new_trade = Trade(trader=current_trader, profit_or_loss=new_profit_or_loss)
    new_trade.save()  # Save the new trade

    # Get the updated list of trades for the trader
    trades = current_trader.trade_set.all()

    timestamps = [trade.timestamp for trade in trades]
    profit_or_loss = [trade.profit_or_loss for trade in trades]

    # Sort the timestamps and profit/loss values together.
    timestamps, profit_or_loss = zip(*sorted(zip(timestamps, profit_or_loss)))

    # Create the plot.
    plt.figure(figsize=(10, 4))
    plt.plot(timestamps, profit_or_loss, label='Profit/Loss')
    plt.xlabel('Timestamp')
    plt.ylabel('Profit/Loss')
    plt.title(f'Dear {current_trader.name}, your Profit/Loss Over Time')
    plt.legend()

    # Save the graph as a base64 encoded image
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    graph_url = base64.b64encode(buffer.read()).decode()
    buffer.close()

    return render(request, 'dashb/user_dashboard.html', {'graph_url': graph_url})

def simulate_profit_or_loss(starting_capital):
    """Simulates the profit or loss on the $100 given to each trader.

    Args:
        starting_capital: The starting capital given to each trader.

    Returns:
        A float representing the profit or loss.
    """

    # Generate a random number between -100 and 100.
    profit_or_loss = random.uniform(-100, 100)

    # Return the profit or loss as a percentage of the starting capital.
    return float(profit_or_loss) / float(starting_capital) * 100

def simulate_profit_or_loss_api(request):
    """API endpoint to simulate profit or loss and return as JSON data."""

    current_trader = Trader.objects.get(user_id=request.user)
    capital = current_trader.starting_capital

    # Simulate a new profit or loss based on the trader's capital
    new_profit_or_loss = simulate_profit_or_loss(capital)

    # Get the existing trades for the trader
    trades = current_trader.trade_set.all()

    # Calculate the new profit or loss based on the previous trades
    if trades:
        previous_profit_or_loss = trades.latest('timestamp').profit_or_loss
        new_profit_or_loss += float(previous_profit_or_loss)

    # Create a new trade with the simulated profit or loss
    new_trade = Trade(trader=current_trader, profit_or_loss=new_profit_or_loss)
    new_trade.save()  # Save the new trade

    # Return the new profit or loss as JSON data
    response_data = {
        'new_profit_or_loss': new_profit_or_loss,
    }
    return JsonResponse(response_data)





def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                user = form.save()

                # Get the username provided by the user
                username = form.cleaned_data.get('username')

                # Create a new Trader object with the user's name and starting capital
                trader = Trader(user=user, name=username, starting_capital=Decimal('100.00'))
                trader.save()

                login(request, user)
                return redirect('index')  # Redirect to the dashboard or any other desired page
    else:
        form = UserCreationForm()
    return render(request, 'dashb/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirect to the dashboard or any other desired page
    else:
        form = AuthenticationForm()
    return render(request, 'dashb/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')