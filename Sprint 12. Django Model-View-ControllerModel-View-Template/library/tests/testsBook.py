from django.test import TestCase
from django.conf import settings


class TestBook(TestCase):
    def test_settings(self):
        self.assertIn("book", settings.INSTALLED_APPS, "book app is not added to settings.py")

    def test_get_minimal_template(self):
        response = self.client.get("/book/")
        content = str(response.content)
        self.assertIn("This is book app page! Congratulations!", content,
                      "GET requests don't return book minimal template")
