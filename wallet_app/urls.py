# wallet_app/urls.py
from django.urls import path
from . import views

app_name = 'wallet_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('account/', views.account_info, name='account_info'),
    path('account/add-phone/', views.add_phone, name='add_phone'),
    path('account/remove-phone/<int:pk>/', views.remove_phone, name='remove_phone'),
    path('account/add-email/', views.add_email, name='add_email'),
    path('account/remove-email/<int:pk>/', views.remove_email, name='remove_email'),
    path('account/add-bank/', views.add_bank_account, name='add_bank_account'),
    path('account/remove-bank/<int:pk>/', views.remove_bank_account, name='remove_bank_account'),
    path('send-money/', views.send_money, name='send_money'),
    path('request-money/', views.request_money, name='request_money'),
    path('statements/', views.statements, name='statements'),
    path('search/', views.search_transactions, name='search_transactions'),
# wallet_app/urls.py
path('complete-transaction/<int:pk>/', views.complete_transaction, name='complete_transaction'),
]