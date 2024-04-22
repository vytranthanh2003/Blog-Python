from django.test import TestCase, SimpleTestCase

# Test bug
class SimpleTest(SimpleTestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)