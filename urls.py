from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('watchlist/add/', views.add_to_watchlist, name='add_to_watchlist'),
    path('alerts/set/', views.set_alert, name='set_alert'),
     path('chart/', views.stock_chart, name='stock_chart'),
]
