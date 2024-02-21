from django.shortcuts import render
from models import Customer, Item, Order
from . import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse


# Create your views here.
@api_view(['GET'])
def get_customers(request):
    customers = Customer.objects.all()
    serializer = serializers.CustomerSerializer(customers, many=True)
    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_customer(request):
    serializer = serializers.CustomerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_orders(request):
    orders = Order.objects.all()
    serializer = serializers.OrderSerializer(orders, many=True)
    return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_order(request):
    serializer = serializers.OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def delete_order(request):
    order = Order.objects.filter(id=id)
    order.delete()
    return Response({"status": "success", "data": "Order successfully deleted"})
