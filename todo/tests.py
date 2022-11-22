from django.test import TestCase
from todo.models import User

class Test_User(TestCase):
    def test_if_take_2_pass(self):
        email = 'user@email.com'
        name = 'Anwar'
        password = '112233'
        password2 = '112233'
        user = User.objects.create_user(email=email, fullname=name, password=password, password2=password2)
        self.assertIs(user.is_staff, False)