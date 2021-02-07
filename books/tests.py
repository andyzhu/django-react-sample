from django.test import TestCase
from .models import Book

# Create your tests here.
class BookTestCase(TestCase):
    def test_book_created(self):
        book_obj = Book.objects.create(name='Anon', author='John Doe', description='anon book')
        self.assertEqual(book_obj.id, 1)