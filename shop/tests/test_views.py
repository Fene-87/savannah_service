from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from shop.models import Item, Order, CustomUser


class ViewsTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@example.com',
            password='testpassword',
            username='testuser',
            customer_code='123456'
        )
        self.item = Item.objects.create(item='Test Item', unit='Piece', price=10.99)

    def test_home_view(self):
        url = reverse('home')
        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/home.html')

    def test_sign_up_view(self):
        url = reverse('sign_up')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/sign_up.html')

        data = {
            'username': 'newuser',
            'password1': 'newpasswor2#d',
            'password2': 'newpasswor2#d',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_get_items_view(self):
        url = reverse('get_items')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/home.html')

    def test_create_order_view(self):
        self.client.force_login(self.user)
        url = reverse('create_order')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/create_order.html')

        data = {
            'item_id': self.item.id,
            'amount': 15.0,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('get_orders'))

    def test_get_orders_view(self):
        url = reverse('get_orders')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/orders.html')
