from django.test import TestCase
from todo.models import User, Todo
from datetime import datetime

class Test_User(TestCase):
    def test_if_take_2_pass(self):
        email = 'user@email.com'
        name = 'Anwar'
        password = '112233'
        password2 = '112233'
        user = User.objects.create_user(email=email, fullname=name, password=password, password2=password2)
        # self.assertIs(user.is_staff, False)
        user2 = User.objects.filter(joined_at__year=datetime.today().year).first()
        from uuid import uuid4
        self.assertIs(user2.fullname, 'Anwar')
    def test_model_response(self):
        all_task = Todo.objects.filter(user_id=1)
        self.assertIs(all_task is not None, True)