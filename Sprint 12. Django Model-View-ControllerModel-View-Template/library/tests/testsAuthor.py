from django.test import TestCase
from django.conf import settings


class TestAuthor(TestCase):
    def test_settings(self):
        self.assertIn("author", settings.INSTALLED_APPS, "author app is not added to settings.py")

    def test_get_minimal_template(self):
        response = self.client.get("/author/")
        content = str(response.content)
        self.assertIn("This is author app page! Congratulations!", content,
                      "GET requests don't return author minimal template")
