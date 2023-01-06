from django.test import TestCase
from django.conf import settings


class TestUser(TestCase):
    def test_settings(self):
        self.assertIn("user", settings.INSTALLED_APPS, "user app is not added to settings.py")

    def test_get_minimal_template(self):
        response = self.client.get("/user/")
        content = str(response.content)
        self.assertIn("This is user app page! Congratulations!", content,
                      "GET requests don't return user minimal template")
