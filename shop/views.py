from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RegisterForm, OrderForm
from .models import CustomUser, Item, Order
from . import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.db.models import F

from .send_sms import send_sms
from .serializers import OrderSerializer


# Create your views here.
@api_view(['GET'])
@login_required(login_url='/login')
def home(request):
    return render(request, 'shop/home.html')


@api_view(['GET', 'POST'])
def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})


@api_view(['GET'])
def get_items(request):
    items = Item.objects.all()
    serializer = serializers.ItemSerializer(items, many=True)
    return render(request, 'shop/home.html', {"items": serializer.data})
    # if request.is_ajax():
    #     return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    # else:
    #     print(items)
    #     return render(request, 'shop/home.html', {"items": serializer.data})


@api_view(['GET', 'POST'])
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            item_id = form.cleaned_data['item_id']
            amount = form.cleaned_data['amount']

            item = get_object_or_404(Item, pk=item_id)
            order = Order.objects.create(customer=request.user, amount=amount)
            order.items.add(item)
            return redirect('get_orders')
    else:
        form = OrderForm()

    return render(request, 'shop/create_order.html', {'form': form})


@api_view(['GET'])
def get_orders(request):
    orders = Order.objects.all()
    # serializer = serializers.OrderSerializer(orders, many=True)

    order_info = []
    for order in orders:
        order_items_info = []

        items = order.items.all()
        for item in items:
            order_items_info.append({
                'item_name': item.item,
                'unit': item.unit,
                'price': item.price
            })

        order_info.append({
            'customer': order.customer.username,
            'time': order.time,
            'amount': order.amount,
            'items': order_items_info
        })

    return render(request, 'shop/orders.html', {"orders": order_info})


@api_view(['POST'])
def delete_order(request):
    order = Order.objects.filter(id=id)
    order.delete()
    return Response({"status": "success", "data": "Order successfully deleted"})
