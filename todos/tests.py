from django.test import TestCase
from .models import Todo

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(title='Messi', body='Not Ronaldo is the best')
    def test_title_content(self):
        self.assertEqual(self.todo.title, 'Messi')
    def test_body_content(self):
        self.assertEqual(self.todo.body, 'Not Ronaldo is the best')