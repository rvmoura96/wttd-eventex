from django.test import TestCase


class HomeTest(TestCase):
    """Tests to Home View"""
    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        """GET / must return status code 200."""
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """Template Used must use index.html."""
        self.assertTemplateUsed(self.response, 'index.html')
