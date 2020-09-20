from django.test import TestCase
from .models import User


class UserModelTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username="test_user", email="testmail@mail.com", password="testpass123")

    def test_user_str_equalto_username(self):
        user = User.objects.get(id=1)
        self.assertEquals(user.__str__(), user.username)
