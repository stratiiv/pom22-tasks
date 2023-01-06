from django.test import TestCase
from django.conf import settings


class TestOrder(TestCase):
    def test_settings(self):
        self.assertIn("order", settings.INSTALLED_APPS, "order app is not added to settings.py")

    def test_get_minimal_template(self):
        response = self.client.get("/order/")
        content = str(response.content)
        self.assertIn("This is order app page! Congratulations!", content,
                      "GET requests don't return order minimal template")
