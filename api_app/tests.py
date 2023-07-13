from django.test import TestCase
from rest_framework.test import APISimpleTestCase,APITestCase
from django.urls import reverse
from rest_framework import status
from .models import CartItem

# Create your tests here.

class CartItemsTest(APITestCase):
    
    def test_post_cart_ıtems(self):
        
        
        url = reverse('cartitems')
        data = {'product_name':'testproduct', 'product_price':152}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CartItem.objects.count(), 1)
        self.assertEqual(CartItem.objects.get().product_name, 'testproduct')
        
        
        
    def test_get_cart_items(self):
        
        url = reverse('cartitems')
        data = {'product_name':'testproduct', 'product_price':152}
        response = self.client.post(url, data, format='json')
        # BURAYA KADAR İTEM OLUŞTURUP POSTLADIM
        
        daa = {} # BURADA DATA NIN GELECEĞİ BOŞ BİR DEĞER ATADIM
        
        response = self.client.get(url, daa, format='json')
        self.assertEqual(CartItem.objects.count(), 1)
        self.assertEqual(CartItem.objects.get().product_name, 'testproduct')