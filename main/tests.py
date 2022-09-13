from django.contrib.auth.models import User
from django.test import TestCase

from project2.main.models import Links

class Test(TestCase):

    def add_url(self):
        self.client.post('/userpage', {'link': 'https://www.yandex.ru' })
        self.client.post('/userpage', {'link': 'https://dzen.ru/?yredirect=true'})
        self.assertTrue(Links.objects.count() == 2)