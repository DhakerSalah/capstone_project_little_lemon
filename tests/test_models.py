
from django.test import TestCase
from restaurant.models import Menu



# Create your tests here.

class MenuTest(TestCase):

    # def test_get_item(self):
    #     item = Menu.objects.create(title='IceCream', price=80, inventory=10)
    #     itemstr = item.get_item()
    #
    #     self.assertEqual(itemstr, "IceCream : 80")

    def test_str(self):
        item = Menu.objects.create(title='IceCream', price=80, inventory=10)
        self.assertEqual(str(item), 'IceCream : 80')
