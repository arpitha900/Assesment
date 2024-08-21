from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'stocks/index.html')

# stocks/views.py

from django.shortcuts import render, redirect
from .models import Watchlist, Alert
from .forms import WatchlistForm, AlertForm



def stock_chart(request):
    return render(request, 'stock_chart.html')

def add_to_watchlist(request):
    if request.method == 'POST':
        form = WatchlistForm(request.POST)
        if form.is_valid():
            watchlist = form.save(commit=False)
            watchlist.user = request.user
            watchlist.save()
            return redirect('watchlist')
    else:
        form = WatchlistForm()
    return render(request, 'add_to_watchlist.html', {'form': form})

def set_alert(request):
    if request.method == 'POST':
        form = AlertForm(request.POST)
        if form.is_valid():
            alert = form.save(commit=False)
            alert.user = request.user
            alert.save()
            return redirect('alerts')
    else:
        form = AlertForm()
    return render(request, 'set_alert.html', {'form': form})
