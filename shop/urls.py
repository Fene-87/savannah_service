from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('orders/', views.get_orders),
    path('items/', views.get_items)
]
