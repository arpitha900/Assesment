import requests
from django.core.management.base import BaseCommand
from stocks.models import Stock

class Command(BaseCommand):
    help = 'Fetch stock data from the API and update the database'

    def handle(self, *args, **kwargs):
        api_key = 'RD4PNKFZWMAJI9TR'
        symbols = ['AAPL', 'GOOGL', 'AMZN']  # Example stock symbols

        for symbol in symbols:
            url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
            response = requests.get(url)
            data = response.json()

            stock, created = Stock.objects.update_or_create(
                symbol=symbol,
                defaults={
                    'name': data['Global Quote']['01. symbol'],
                    'current_price': data['Global Quote']['05. price'],
                }
            )
            self.stdout.write(self.style.SUCCESS(f'Successfully updated {stock.name}'))
