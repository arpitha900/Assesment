from django import forms
from .models import Watchlist, Alert

class WatchlistForm(forms.ModelForm):
    class Meta:
        model = Watchlist
        fields = ['stock']

class AlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ['stock', 'price_target']
