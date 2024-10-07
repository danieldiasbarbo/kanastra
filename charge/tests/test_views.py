from django.test import TestCase, Client
from django.urls import reverse
from charge.dtos import DebtDTO
import os


class testViews(TestCase):
    def test_csv_processing(self):
        with open(r".\charge\tests\cosntants\valid_example_file.csv", "rb") as csv_file:
            client = Client()
            response = client.post(reverse("csv"), {"file": csv_file})
            self.assertEqual(response.status_code, 200)

    def test_csv_processing_with_duplicates(self):
        with open(
            r".\charge\tests\cosntants\example_file_with_duplicates.csv", "rb"
        ) as csv_file:
            client = Client()
            response = client.post(reverse("csv"), {"file": csv_file})
            self.assertEqual(response.status_code, 200)

    def test_csv_processing_with_missing_fields(self):
        with open(
            r".\charge\tests\cosntants\example_file_missing_email.csv", "rb"
        ) as csv_file:
            client = Client()
            response = client.post(reverse("csv"), {"file": csv_file})
            self.assertEqual(response.status_code, 400)

    def test_csv_processing_with_missing_fields(self):
        with open(r".\charge\tests\cosntants\not_csv_file.txt", "rb") as file:
            client = Client()
            response = client.post(reverse("csv"), {"file": file})
            self.assertEqual(response.status_code, 400)

    def test_get_is_not_allowed(self):
        with open(r".\charge\tests\cosntants\valid_example_file.csv", "rb") as csv_file:
            client = Client()
            response = client.get(reverse("csv"), {"file": csv_file})
            self.assertEqual(response.status_code, 405)

    def test_put_is_not_allowed(self):
        with open(r".\charge\tests\cosntants\valid_example_file.csv", "rb") as csv_file:
            client = Client()
            response = client.put(reverse("csv"), {"file": csv_file})
            self.assertEqual(response.status_code, 405)

    def test_delete_is_not_allowed(self):
        with open(r".\charge\tests\cosntants\valid_example_file.csv", "rb") as csv_file:
            client = Client()
            response = client.put(reverse("csv"), {"file": csv_file})
            self.assertEqual(response.status_code, 405)
