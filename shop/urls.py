from django.urls import path
from . import views
from allauth.account.views import LoginView, SignupView

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.get_items, name='get_items'),
    path('create-order/', views.create_order, name='create_order'),
    path('order-list/', views.get_orders, name='get_orders'),
    path('orders/', views.get_orders),
    path('sign-up', views.sign_up, name='sign_up'),
]
