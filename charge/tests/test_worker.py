from django.test import SimpleTestCase
from charge.worker import Worker
from charge.tests.cosntants.constants import (
    simple_list_debt_dto,
    list_debt_dto_with_duplicates,
)


class TestWorker(SimpleTestCase):
    def test_emails_sent(self):
        worker = Worker()
        with open(r".\charge\tests\cosntants\valid_example_file.csv", "rb") as csv_file:
            result = worker.async_debt_processing(simple_list_debt_dto)
            assert simple_list_debt_dto == result

    def test_emails_sent_with_duplicates(self):
        worker = Worker()
        print(f"SET JÁ PROCESSADO: {worker.processed_debts_db}")
        with open(r".\charge\tests\cosntants\valid_example_file.csv", "rb") as csv_file:
            result = worker.async_debt_processing(list_debt_dto_with_duplicates)
            assert list_debt_dto_with_duplicates[:-1] == result
