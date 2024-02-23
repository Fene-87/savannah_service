import datetime
from unittest.mock import patch, MagicMock
from _pytest import unittest
from django.test import TestCase
from django.contrib.auth import get_user_model
from pytest_mock import mocker

from shop.models import CustomUser, Item, Order


class CustomUserModelTest(TestCase):
    def test_create_user(self):
        user = get_user_model().objects.create_user(
            email='test@example.com',
            password='testpassword',
            username='testuser',
            customer_code='123456'
        )
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.customer_code, '123456')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)

    def test_create_superuser(self):
        admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='adminpassword',
            username='adminuser',
            customer_code='654321'
        )
        self.assertEqual(admin_user.email, 'admin@example.com')
        self.assertEqual(admin_user.username, 'adminuser')
        self.assertEqual(admin_user.customer_code, '654321')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class OrderModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            password='testpassword',
            username='testuser',
            customer_code='123456'
        )
        self.item = Item.objects.create(item='Test Item', unit='Piece', price=10.99)

    @patch('shop.models.africastalking.SMS')
    def test_create_order(self, mock_sms):
        mock_sms.return_value = MagicMock()
        order = Order.objects.create(
            customer=self.user,
            amount=50.45
        )
        order.items.add(self.item)
        self.assertEqual(order.customer, self.user)
        self.assertEqual(order.amount, 50.45)
        self.assertEqual(order.items.first(), self.item)
        self.assertTrue(isinstance(order.time, datetime.datetime))
