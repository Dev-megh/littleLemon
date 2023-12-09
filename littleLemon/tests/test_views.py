from django.test import TestCase
from restaurant.models import Booking, Menu
from django.urls import reverse

class MenuViewTest(TestCase):
	def setUp(self):
		Menu.objects.create(title="IceCream", price=80, inventory=100)
		Menu.objects.create(title="Pizza", price=100, inventory=50)

	def test_getall(self):
		response = self.client.get(reverse('menu'))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(len(response.data), 2)
		self.assertEqual(response.data[0]['title'], 'IceCream')
		self.assertEqual(response.data[1]['title'], 'Pizza')