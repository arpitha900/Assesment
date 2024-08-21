from django.test import TestCase
from django.urls import reverse
# Create your tests here.

from .models import Stock

class StockModelTest(TestCase):

    def test_stock_creation(self):
        stock = Stock.objects.create(symbol='AAPL', name='Apple Inc', current_price=150.00)
        self.assertEqual(stock.symbol, 'AAPL')

    # stocks/tests.py




class WatchlistTests(TestCase):
    def test_add_to_watchlist_view(self):
        response = self.client.get(reverse('add_to_watchlist'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_to_watchlist.html')

    def test_set_alert_view(self):
        response = self.client.get(reverse('set_alert'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'set_alert.html')

