from django.test import TestCase
from django.urls import reverse
# Create your tests here.
class SnacksTest(TestCase):
    def test_snack_status_code(self):
        url = reverse('snackes_lists')
        actual = self.client.get(url).status_code
        expected = 200
        self.assertEqual(expected, actual)

    def test_snack_template(self):
        url = reverse('snackes_lists')
        response = self.client.get(url)
        actual = 'snackes_lists.html'
        self.assertTemplateUsed(response, actual)
