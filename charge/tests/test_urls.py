from django.test import SimpleTestCase
from django.urls import reverse, resolve
from charge.views import upload_csv


class TestUrls(SimpleTestCase):
    def test_charge_csv_resolves(self):
        url = reverse("csv")
        print(resolve(url))
        self.assertEqual(resolve(url).func, upload_csv)
