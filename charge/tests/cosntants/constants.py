from charge.dtos import DebtDTO

simple_list_debt_dto = [
    DebtDTO(
        name="John Doe",
        government_id="11111111111",
        email="johndoe@kanastra.com.br",
        debt_amount="1000000.00",
        debt_due_date="2022-10-12",
        debt_id="1adb6ccf-ff16-467f-bea7-5f05d494280f",
    ),
    DebtDTO(
        name="Person Name",
        government_id="11111111112",
        email="person@kanastra.com.br",
        debt_amount="105000.00",
        debt_due_date="2024-11-01",
        debt_id="2adb6ccf-ff16-467f-bea7-5f05d494280a",
    ),
    DebtDTO(
        name="Person Name",
        government_id="11111111112",
        email="person@kanastra.com.br",
        debt_amount="105000.00",
        debt_due_date="2024-11-01",
        debt_id="2adb6ccf-ff16-467f-bea7-5f05d494280b",
    ),
]

list_debt_dto_with_duplicates = [
    DebtDTO(
        name="John Doe",
        government_id="11111111111",
        email="johndoe@kanastra.com.br",
        debt_amount="1000000.00",
        debt_due_date="2022-10-12",
        debt_id="1adb6ccf-ff16-467f-bea7-5f05d494280f",
    ),
    DebtDTO(
        name="Person Name",
        government_id="11111111112",
        email="person@kanastra.com.br",
        debt_amount="105000.00",
        debt_due_date="2024-11-01",
        debt_id="2adb6ccf-ff16-467f-bea7-5f05d494280a",
    ),
    DebtDTO(
        name="Person Name",
        government_id="11111111112",
        email="person@kanastra.com.br",
        debt_amount="105000.00",
        debt_due_date="2024-11-01",
        debt_id="2adb6ccf-ff16-467f-bea7-5f05d494280a",
    ),
]
